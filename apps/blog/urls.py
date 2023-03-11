from django.urls import path
# from .views import BlogListView, ListPostsByCategoryView, PostDetailView
from .views import *

urlpatterns = [
    path('list', BlogListView.as_view(), name='BlogList'),
    path('by_category', ListPostsByCategoryView.as_view(), name='ListPostsByCategory'),
    path('detail/<slug>', PostDetailView.as_view(), name='PostDetail'),
    path('search', SearchBlogView.as_view(), name='SearchBlog'),
]
