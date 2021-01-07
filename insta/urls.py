from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from profiles.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',profile)

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
