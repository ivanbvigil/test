from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views




urlpatterns = [
    path('create/', views.create, name = 'create'),
    path('<int:task_id>', views.detail, name= 'detail'),
    path('<int:task_id>/state_change', views.state_change, name= 'state_change'),
    path('<int:task_id>/state_change_home',views.state_change_home, name = 'state_change_home'),
    path('<int:task_id>/update', views.update, name = 'update'),
    path('<int:task_id>/update_submit',views.update_submit, name = 'update_submit'),
	path('<int:task_id>/delete', views.delete, name = 'delete'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

