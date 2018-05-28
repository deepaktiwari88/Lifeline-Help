from django.conf.urls import url
from temp import views

app_name = 'temp'

urlpatterns = [

    url( r'signup/$' , views.signup_view , name="signup"),
    url( r'login/$' , views.login_view , name="login"),
    url( r'logout/$' , views.logout_view , name = "logout"),
   url( r'home/$' , views.home , name="home"),
]