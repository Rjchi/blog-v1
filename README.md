NOTA: Hacer el (npm)build y al (python)collectstatic

.env del directorio base = REACT_APP_API_URL='http://127.0.0.1:8000'

.env del backend = 

SECRET_KEY='pd45@@hw2y4te2#1y8c99-_8$e(6s9^gv23a8-frt0euu)+k(m'
DEBUG=True

DATABASE_URL=''

ALLOWED_HOSTS_DEV='*'
ALLOWED_HOSTS_DEPLOY='otro.com', 'www.otro.com'

CORS_ORIGIN_WHITELIST_DEV='http://localhost:3000'
CORS_ORIGIN_WHITELIST_DEPLOY='https://otro.com'

CSRF_TRUSTED_ORIGINS_DEV='http://localhost:3000'
CSRF_TRUSTED_ORIGINS_DEPLOY='https://otro.com'




Nota: Instalar potsman

Nota: Cuando una seccion tiene paginas unicas en estilos por lo general es una pagina estatica
	ya que las dinamicas por lo general utilizan templetes donde condicionan todo para que el contenido vaya cambiando
	pero la plantilla es la misma.
	
	Siempre que vamos a implementar contenido que es dinamico empezamos con el backend.
	este va  a crear los modelos(post (con sus atributos)) que van a ser empujados a la base de datos 
	(entendiendo como modelo la estructura de la pagina que vamos 
	a utilizar header=title - categoria, main=description etc)

20. Ahora para migrar un proyecto lo que tenemos que hacer es crear una carpeta nueva dentro de la carpeta contenedora 
	llamada blog_personal(en mi caso) Curso_DRF/blog_personal
21. Ahora en el proyecto que teniamos seleccionamos todo menos env, node_modules y package-lock.json
	y lo pegamos en blog_personal
22. Ahora en una terminal creamos nuevamente un ambiente virtual python -m virtualenv env y lo activamos
23. Ahora ejecutamos pip install -r requirements.txt
24. Ahora en otra terminal ejecutamos npm i (es como crear el ambiente virtual para react) y con esto ya tenemos nuestra migracion
25. Ahora desde el cmd nos ubicamos en cd apps (Antes de empezar publicarlo en Github y trabajamos desde staging)
26. Ahora en el cmd creamos una nueva aplicacion python ..\manage.py startapp blog (ver posicionamiento en el directorio)
27. Ahora en cmd creamos otra aplicacion llamada python ..\manage.py startapp categoty
28. Ahora le creamos un archivo a cada uno llamado urls.py
29. Ahora despues de crear los modelos vamos a hacer una migracion ejecutando cd .. y python manage.py makemigrations
	con esto se crean los modelos para las tablas
30. Ahora para hacer la migracion de estas tablas ejecutamos python manage.py migrate
31. Ahora creamos un nuevo archivo en category/ llamado serializers.py
32. Ahora creamos las vistas
33. Ahora ejecutamos python manage.py createsuperuser y creamos un super usuario y agregamos unas cuatas categorias y subcategorias
34. Ahora probamos la primera vista con postman | class ListCategoriesView
35. Ahora en blog creamos un archivo llamado serializers.py
36. Ahora hacemos un nuevo build de nuestro proyecto y tambien eliminamos static(los que ya teniamos) y comentamos lo que hicimos en github
	pero no sincronizamos
37. Ahora en el cmd de react ejecutamos npm run build
38. Ahora en el cmd de python ejecutamos python manage.py collectstatic
39. Ahora en blog creamos un archivo llamado pagination.py (para que cuando llamamemos la api (la lista de post) no nos traiga todos los 
	posts de golpe (err505))
	Siempre que listemos debemos paginar
40. Ahora creamos un nuevo archivollamado .env en el directorio base (va a contener la url de la API de nuestro 
	backend = http://127.0.0.1:8000)
	este es el env 	que pertenece al frontend (react) y esto va a juntarce cuando hagamos build
41. Ahora en src/components creamos una nueva carpeta llamada blog

Vamos a utilizar ridux para el llamado de la api:

42. Ahora en redux/actions creamos dos carpetas llamadas blog y categories
43. Ahora en categories creamos un nuevo archivo llamado categories.js y otro llamado types.js (siempre lo debemos tener)
44. Ahora en blog cremos un nuevo archivo llamado types.js y otro llamado blog.js
45. Ahora en reducers creamos un nuevo archivo llamado categories.js(aqui definimos el estado de lo que llamamos con la API)
	osea donde guardamos el resultado de la api para poder acceder posteriormente
	tambien lo debemos registrar en el reducers/index.js
46. Ahora hacemos lo mismo para blog(tener en cuenta las views.py de blog)

NOTA: cuando indiquemos como variable de entorno el ip donde se encuentra nuestra api, debemos cerrar el frontend para que nos tome los cambios
	y cuando usemos la api debe estar el backend corriendo
Front end
47. Ahora en conponents/ Creamos un nuevo archivo llamado BlogCateHeader.js (aqui va a estar las categorias que vienen desde la api)
48. Ahora en pages/ creamos un nuevo archivo llamado Category.jsx
49. Ahora en pages/ creamos un nuevo archivo llamado Search.jsx
50. Ahora en components/blog/ creamos dos nuevos archivos llamados BlogList.js y BlogCardHorizontal.js
51. Ahora en components/creamos una carpeta llamada pagination y un nuevo archivo llamado SmallSetPagination.js
52. Ahora en components/blog/ creamos un nuevo archivo llamado BlogCardSearch.js
53. Ahora creamos un archivo en pagination/ llamado SmallSetPaginationSearch.js
54. Ahora en components/ creamos una carpeta llamada search y dentro de ella creamos un archivo llamado BlogList.js
55. Ahora en pages/ creamos un nuevo archivo llamado PostDetail.jsx
56. Ahora en la terminal del front end ejecutamos npm i dompurify (esto nos permite proteger la informacion que estamos mostrando para cada post
	esto lo hacemos (cuando vamos a mostrar contenido que tiene html en este caso el campo content que hace uso de ckeditor))

