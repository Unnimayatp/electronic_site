
from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('signup/',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('home/',views.home,name='home'),

]
