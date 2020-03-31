# Django-Dashboard MVG (Modelo-Vista-Graficar)

Antes que nada, debemos saber que es un dashboard, un Dashboard no es mas que una tabla que de manera dinamica aumenta o disminuye en función de los datos obtenidos de lo cual un conjunto de gráficos representa un DASHBOARD, estos Dashboard puede obtener algunos de los siguiente graficos:

- Circular
- Pastel
- Lineal
- Polar
- Ares y demás.

La idea de todo esto es poder entender utilidad y como podemos desarrollarlo, en el aspecto de la utilizada, los gráficos hablan mas que los datos suministrados, para que estos datos e información puedan ser procesada y en virtud de la misma graficadas, requerimos de uno o varios modelos en función de lo que queremos graficar.

Ahora bien utilizaremos unos de los Framework que para mi uso personal es muy sostenible y fácil de usar a la hora de crear Modelo, Vista y Graficar, este paradigma nos ayuda a realizar en tampoco tiempo un trabajo. Y veremos como hacerlo utilizando Django y la librerías de Javascript.

##
## [Creando nuestro primer proyecto](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

```
@jeancharlyjs$ django-admin startproject dashboard-django
```

Con este comando creamos los archivos fundamentales para poder trabajar con el Framework, django de por si contiene unos archivos que se puede configurar como lo es el [SETTINGS](https://docs.djangoproject.com/en/3.0/ref/settings/), en esta documentación puede encontrar mas detalles. Luego de haber creado el proyecto, este nos devuelve dos tipos de archivos, tal archivo es la carpeta del proyecto y un archivo llamado **manage.py**, este archivo es quien se encarga de crear app, correr el servidor, ya que **Django** nos da dicha facilidad y no obstante a ello este archivo nos permite  acceder mediante el siguiente comando a una **SHELL**.

```
@jeancharlyjs$ python manage.py shell #Este nos permirte obtener una shell
```

Es indispensable crear la aplicación de la cual se va a trabajar, en dicha aplicación es donde estaremos creando nuestro Modelo, Vista, Ruta y Template(Gráficos), esto se crea de la siguiente forma.

```
@jeancharlyjs$ python manage.py startapp [NOMBRE DE LA APP] #python manage.py dashboardapp
```

```bash
@jeancharlyjs$ ls dashboard-djangoproject
dashboad-django  dashdjango manage.py
```
## PRIMERA PARTE
## Modifica SETTINGS
###### Installed APPS
Lo primero que se hará después de crear **djangoapp** es modificar el **SETTINGS** debido a que debemos agragar nuestro app a la variable  _ INSTALLED_APPS_ ya  creada. Esto se realiza de la siguente manera.:
</br>
**settings.py**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'dashdjangoapp', #Este app fue quien creamos mas arriba con python manage.py startapp
]
```
Dentro del mismo **SETTINGS** podemos realizar muchas demás cosas, tal cual es leer un archivo como es el caso del _Templates_, _Bases de Datos [PostgreSQL]_


###### [TEMPLATES](https://docs.djangoproject.com/en/3.0/topics/templates/)

Para este caso, primero debemos crear un carpeta con el nombre **Templates**, esta carpeta obtendrá todo los archivos plantillas, como lo es:

- HTML
</br>

**settings.py**

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #BASE_DIR(Es una variable ya creada, de lo cual podemos llamarla y os.path.join() se encarga del resto. 'templates' hace referencia a la carpeta creada 'mkdir tamplates' [Si estan utilizando GNU/Linux])
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
###### [Static ](https://docs.djangoproject.com/en/3.0/howto/static-files/)
Dentro de la programación y mas ahora en este Framework los archivos *estáticos* son aquellos archivos que se mantienen constante en su naturaleza pero no en su ejecución, tales archivos son:

- Javascript
- CSS

Tanto *Javascript* como *CSS* no son estáticos, ya que realizan acciones en función de un hecho, la razón por la cual se le considera **ESTÁTICO** es que esta no afecta a los documentos de naturaleza Django de forma directa, pero si afecta de forma indirecta. ES IMPORTANTE ENTENDER ESTO.

**settings.py**
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```
## Creando el Superusuario
Ya en este parte hemos avanzado mucho,  el **Superusuario** es el responsable de administrar los recursos... En este caso de _Django_ y es quien tiene todos los privilegios en el Framework, pero para ello debemos crearlo de la siguiente manera. Pero antes de proceder a crear el Superusuario, debemos de crear las _tablas_ en la base de datos, es importante hacer esto ya que es quien nos permite registrar todo el contenido del **SETTINGS**

```bash
jeancharlyjs$ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK

```
Esto a su vez crea un archivo llamado _db.sqlite3_, si la variable **DATABASES** en el settings no esta configurada con un motor de Base de datos, Django agrega lo antes mencionada por defecto.

```bash
jeancharlyjs$ python manage.py createsuperuser
Username (leave blank to use '[usuario/GNULinux]'): admin
Email address: jean@admin.com    
Password:
Password (again):
Superuser created successfully.
```
Con esta operación estaremos creando el usuario [que de mi parte le llamare *admin*] y su contraseña. **Luego de esta operación podemos correr el servidor**
con la siguiente acción.

```bash
jeancharlyjs$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 26, 2020 - 21:34:50
Django version 2.2.4, using settings 'dashdjango.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Lugo podemos ir a nuestro Browers y escribir en la barra de _url_  **localhost:8000**
![Browers localhost](https://github.com/jeancharlyjs/dashboard-django/blob/master/dashdjango/static/imag/RunServer.png)

<br>
</br>

En esta misma linea, si queremos acceder al admin, solo tenemos que agragar **localhost:8000/admin**
![Admin](https://github.com/jeancharlyjs/dashboard-django/blob/master/dashdjango/static/imag/BrowersAdmin.png)

<br>
</br>

## SEGUNDA PARTE


**Esquema de directorios y archivos**
```
├── dashdjango
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dashdjangoapp
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── static
└── templates
    └── index.html
```

Después de haber creado y configurado los archivos correspondiente procedemos a explicar en que consiste esta parte.

Aquí en lo adelante estaremos trabajo con dos directorios que son **Templates** y **Static**, es indispensable haber creado estas carpetas y no menos importante haberla configurado en el , de lo cual nos permitirá poder leer una extension .html desde nuestra Vista llamando esta con la URL.

</br>

Para poder realizar esto lo que debemos hacer es editar un archivo y es: la **Views** y crear una llamada **urls.py**, en esta urls.py solo agregaremos los nombre de la función que estarán en nuestra **Views.py** de lo  cual se estarán importando.

**Ejemplo**
</br>

**views.py**
```python
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class index(View):
    def get(self, request, *args, **kwargs):
        context = {
            "Tesla" : "Nikola Tesla - Genio por Excelencia"
        }
        return render(request, "index.html", context)


```

</br>

Como podemos observar, este pedazos de código, nos indica lo siguiente:
En donde llamamos una Views genérica y se la atribuimos a la _clase_, a esta les indicamos un nombre, nombre que para a ser de la **urls.py**, luego declaramos una función quien obtiene los valores, estos valores pasan a ser un método del objecto, donde este método retorna un valor y he aquí lo interesante...

```python
return render(request, "index.html", context)
```
El **Render** tomo los valores **REQUEST** que solicita del **"index.html"** este segundo parámetro es donde se estarán colocando los archivos **HTML** que se agreguen al _Templates_, si que crea una función diferente de lo cual renderizar un pagina diferente, entonces este debe ser un HTML diferente, y por ultimo esta el **CONTEXT {}**, este tercer parámetro adquiere los valores tipo diccionario para enviarlo al html.

Para cada función si y solo si es necesario le corresponde una *URL*, estas urls se estarán colocando en el archivo _urls.py_ que creamos en nuestra aplicación.

**urls.py**

```python
from django.conf.urls import url
from .views import index, VisualizadorJSON

urlpatterns = [
        url(r'^$', index.as_view(), name="index"),
        url(r'^datos/$', VisualizadorJSON.as_view(), name="dash"),
]

```
Luego de esto debemos indicarle a la **url del proyecto** la importación de la misma.

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashdjangoapp.urls')),
]
```
Y para terminar de "CONFIGURAR" por código, debemos crear nuestro **index.html** y listo. Ahí tendremos nuestra WEB.

![Nikola Tesla](https://github.com/jeancharlyjs/dashboard-django/blob/master/dashdjango/static/imag/Nikola%20Tesla.png)

## TECERA PARTE

Ya para esta parte realizaremos las integraciones correspondiente a la *DASHBOARD* pero no si antes realizar las configuraciones correspondiente en la _views.py_ , es importante saber que necesitaremos de algunas otras tecnología como lo es *AJAX*, ya que esta nos permite modular la información.

En lo adelante trabajaremos con un nuevo archivo Javascript que le llamaremos **chart.js**, como antes hemos explicado  que los archivo estáticos se debe almacenar en la carpeta creada llamada **static**, que a su vez es buena practica separarlo mediante nuevas carpetas los **Javascript y los CSS**.

Esto nos quedaría quedando de la siguiente forma:

**chart.js**
```js
var datosurl = '/datos/'
$.ajax({
  method:"GET",
  url: datosurl,
  success: function(dato){
    // Variable de la Views.py
    labels = dato.labels
    cientificos = dato.cientificos
    dashchart()
  },
  error: function(error_data){
    console.log("error")
    console.log(error_datos)
  }
})
function dashchart(){
  var ctx = document.getElementById('myChart').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: cientificos,
          datasets: [{
              label: '# of Votes',
              data: labels,
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero: true
                  }
              }]
          }
      }
  })
};

```
Y para el HTML seria lo siguiente:

**index.html**
```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Nikola Tesla</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  </head>
  <body>
    <div class="container py-5">
      <h1>{{ Tesla }}</h1>
      <hr>
    </div>
    <div class="row">
      <div class="col-1">
      </div>
      <div class="col-4">
        <img alt="Nikola Tesla, el hombre que cambió el mundo" class="n3VNCb" src="https://img-cdn.hipertextual.com/files/2014/06/Nikola-Tesla.jpg?strip=all&amp;lossy=1&amp;quality=70&amp;resize=740%2C490&amp;ssl=1" data-noaft="1" jsname="HiaYvf" jsaction="load:XAeZkd;" style="width: 527px; height: 348.959px; margin: 0px;">
        <h3 class="text-center"><em>"El presente es de ellos, pero el futuro, por el cual trabajé tanto, es mío".</em></h3>
      </div>
      <div class="col-1">
      </div>
      <div id="chartjs-contener" class="col-5" style="width: 100%; height: 80% backgroundColor: black">
        <h3 class="text-right">Dashboard Example...</h3>
        <canvas id="myChart"></canvas>
        <button id="actualizar" type="button" class="btn btn-secondary btn-lg btn-block " style="background-color:#8b8bc0" onclick="actualizar()">Actualizar Datos</button>
      </div>
    </div>
    <div class="container">
      <hr>
    </div>
    <script>
    function actualizar(){
      document.getElementById("chartjs-contener").innerHTML = location.reload();
    }
    </script>
    <script type="text/javascript" src="{% static 'js/jquery.js'%}"></script>
    <script type="text/javascript" src="{% static 'js/chart.js' %}"></script>
  </body>
</html>

```
Este seria un esquema básico para construir el **DASHBOARD** pero no es lo suficiente, debido que queremos tomar los valores desde nuestra _views.py_ , lo que haremo es crear una función que nos almacenará los valores tipo **JSON**, estos valores a su vez deberán ser enviando a una URL, esta URL a la misma vez deberá ser leída por **AJAX**, con la finalidad de poder presentar los datos de la **Views.py** en nuestro _index.html_ .

Y para nuestro archivo _views.py_ todo queda expuesto en donde creamos nuestra función y se la pasamos a la _urls.py_ de nuestro aplicación de la siguiente manera.

**views.py**
```python
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Rest Framework
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class index(View):
    def get(self, request, *args, **kwargs):
        context = {
            "Tesla" : "Nikola Tesla - Genio por Excelencia"
        }
        return render(request, "index.html", context)


class VisualizadorJSON(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        from random import sample
        cientificos = ['Nikola Tesla', 'Isaac Newton', 'Nicolas Copernico', 'Maria Curie', 'Arquimedes', 'Erwin Schrödinger']
        lista = list(range(80))
        puntos = sample(lista, 6)
        # puntos = [50, 19, 3, 5, 2, 3]
        datos = {
                "labels": puntos,
                "cientificos": cientificos
        }
        return Response(datos)
```
Es importante saber y tener conocimiento de las APIs en este caso [Rest_Framework](https://www.django-rest-framework.org/) en donde nos permite serializadores o visualizar los datos de nuestro modelos, permitiendo obtener el diccionario tipo JSON capturandolo con un _Response_ [Breve Documentación Rest-Django](https://www.paradigmadigital.com/dev/introduccion-django-rest-framework/).
En donde **JsonResponse** adquiere los valores y este son pasado a la url tipo JSON y no obstante podemos ingresar mediante la url **localhost:8000/datos** y nos devolverá los valores tipo JSON en nuestro navegador.

**urls.py**

```python
from django.conf.urls import url
from .views import index, VisualizadorJSON

urlpatterns = [
        url(r'^$', index.as_view(), name="index"),
        url(r'^datos/$', VisualizadorJSON.as_view(), name="dash"),
]
```
Y esta es la manera en la que se muestra.

![Dashboard](https://github.com/jeancharlyjs/dashboard-django/blob/master/dashdjango/static/imag/DashboardTesla.png)

![Rest-API](https://github.com/jeancharlyjs/dashboard-django/blob/master/dashdjango/static/imag/DatosApiRest.png)

Como ya hemos definido en nuestra URL para manejo de los datos en la aplicacion nuestra, podemos visualizar con propiedad esta información de la accediendo a la url **localhost:8000/datos/** que como se menciono, nos devolverá un JSON haciendo referencia a nuestra **view.py** de la siguiente forma.
