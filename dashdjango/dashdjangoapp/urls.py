from django.conf.urls import url
from .views import index, VisualizadorJSON

urlpatterns = [
        url(r'^$', index.as_view(), name="index"),
        url(r'^datos/$', VisualizadorJSON.as_view(), name="dash"),
]
