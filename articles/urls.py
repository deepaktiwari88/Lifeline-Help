from django.conf.urls import url
from . import views

app_name = "articles"

urlpatterns = [
    url(r'^$', views.index, name='article'),
    url(r'^index/$', views.index, name='art'),
    url(r'^write/$' , views.write , name='write'),
]
