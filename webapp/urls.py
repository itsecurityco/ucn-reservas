from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('devices/', views.devices_index, name='devices'),
    path('borrow/', views.borrow_post, name='borrow_post'),
]