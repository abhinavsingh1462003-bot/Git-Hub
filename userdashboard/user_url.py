from .import views
from django.urls import path

urlpatterns = [
    path('', views.HOME_Main_Page, name='Startpage'),
    path('home/', views.home, name='home'),
    path("login/", views.login, name='login page'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("logout/", views.logout, name='logout user'),
]
