from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', views.calc, name='calc'),
    path('history/', views.history, name='history'),
    path('result/', views.result, name='result'),
    path('result/<int:res_id>/', views.result, name='result'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
	path('logout/', views.logout, name='logout'),
	path('help/', views.help, name='help'),
]
