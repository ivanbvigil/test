from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import tasks.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasks.views.home, name = 'home'),
    path('accounts/', include('accounts.urls'), name = 'accounts'),
    path('tasks/', include('tasks.urls'), name = 'tasks'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
