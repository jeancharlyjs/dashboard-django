from django.conf.urls import url
from .views import index, dashboard

urlpatterns = [
        url(r'^$', index.as_view(), name="index"),
        url(r'^datos/$', dashboard, name="dash"),
]
