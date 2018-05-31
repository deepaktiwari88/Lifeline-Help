from django.conf.urls import url
from temp import views

app_name = 'temp'

urlpatterns = [

    url( r'welcome/$' , views.formhandleview , name="form"),
    url( r'logout/$' , views.logout_view , name = "logout"),
   url( r'home/$' , views.home , name="home"),
]