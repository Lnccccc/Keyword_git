from django.urls import path

from . import views
app_name='login'
urlpatterns = [
    path("",views.first,name='login'),
    path("welcome/",views.login,name='welcome'),
    path("register/",views.register,name='register'),
    path("logout/",views.logout,name='logout'),
]