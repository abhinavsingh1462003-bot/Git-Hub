from django.urls import path
from . import views

urlpatterns = [
    path('', views.HOME_Main_Page, name='home_main'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('newuser/', views.newuser, name='newuser'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('changepassword/', views.changepassword, name='changepassword'),
]
