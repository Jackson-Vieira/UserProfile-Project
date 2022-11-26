from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import SimpleRouter

from users.api import views

urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


router = SimpleRouter()

# API V1
router.register('users', views.UserViewSet)

urlpatterns += path('api/v1/', include(router.urls)),