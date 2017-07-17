from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello/$', views.index, name='index'),
    url(r'^image/$', views.upload_file, name='upload_file')
]