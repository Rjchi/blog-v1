from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from apps.category.models import Category

from .serializers import PostSerializer, PostListSerializer
from .models import ViewCount, Post

from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination

from django.db.models.query_utils import Q


class BlogListView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Post.post_objects.all().exists():

            posts = Post.post_objects.all()

            # Pagination:

            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(posts, request)

            # Many porque van a ser una lista de posts
            serializer = PostListSerializer(results, many=True)

            # return Response({'Post': serializer.data}, status=status.HTTP_200_OK)
            return paginator.get_paginated_response({'posts': serializer.data})
        else:
            return Response({'Error': 'Not posts found'}, status=status.HTTP_404_NOT_FOUND)


class ListPostsByCategoryView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Post.post_objects.all().exists():

            # Esto es igual a urls = test | list/by_category?slug=test ...
            slug = request.query_params.get('slug')
            # Tomamos la categoria por su slug
            category = Category.objects.get(slug=slug)

            # Mostramos los mas nuevos con order_by()
            posts = Post.post_objects.order_by('-published').all()

            if not Category.objects.filter(parent=category).exists():
                posts = posts.filter(category=category)
            else:
                sub_categories = Category.objects.filter(parent=category)
                # Category:
                filtered_categories = [category]

                for cate in sub_categories:
                    filtered_categories.append(cate)
                filtered_categories = tuple(filtered_categories)
                posts = posts.filter(category__in=filtered_categories)

            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(posts, request)
            serializer = PostListSerializer(results, many=True)
            # return Response({'Test': 'Success'}, status=status.HTTP_200_OK)

            return paginator.get_paginated_response({'posts': serializer.data})

        else:
            return Response({'Error': 'Not posts found'}, status=status.HTTP_404_NOT_FOUND)


class PostDetailView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, slug, format=None):
        if Post.post_objects.filter(slug=slug).exists():
            post = Post.post_objects.get(slug=slug)
            # Aqui como solo toma un resultado no le decimos many=True
            serializer = PostSerializer(post)

            address = request.META.get('HTTP_X_FORWARDED_FOR')
            # Si es que obtenemos un address:
            if address:
                ip_address = address.split(',')[-1].strip()
            else:
                # Si no lo tomamos asi:
                ip_address = request.META.get('REMOTE_ADDR')

            if not ViewCount.objects.filter(post=post, ip_address=ip_address):
                view = ViewCount(post=post, ip_address=ip_address)
                view.save()
                post.views += 1
                post.save()
            return Response({'post': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Post does not exists'}, status=status.HTTP_404_NOT_FOUND)


class SearchBlogView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        search_term = request.query_params.get('s')
        # Filtros Q (nos permite filtrar por varios campos)
        # con __ accedemos a un campo especifico campoDelmodelo__name
        matches = Post.post_objects.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(content__icontains=search_term) |
            Q(category__name__icontains=search_term)
        )

        paginator = SmallSetPagination()
        results = paginator.paginate_queryset(matches, request)

        serializer = PostListSerializer(results, many=True)
        return paginator.get_paginated_response({'filtered_posts': serializer.data})
