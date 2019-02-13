from django.contrib import admin
from django.urls import path, include
import tasks.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasks.views.home, name = 'home'),
    path('accounts/', include('accounts.urls'), name = 'accounts'),
    path('tasks/', include('tasks.urls'), name = 'tasks'),
]
