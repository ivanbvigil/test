from django.contrib import admin
from django.urls import path, include
import accounts.views as views

urlpatterns = [
	path('signup',views.signup, name = 'signup'),
#    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
]