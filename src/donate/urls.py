from django.conf.urls import url
from .views import index,confirm

app_name = "donate"

urlpatterns = [
    url(r'^$', index , name='index'),
    url(r'^confirm/$', confirm, name='confirm')
]