from django.contrib import admin
from django.urls import path, include
from . import yasg_schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('auth/', include('users.urls')),
]

urlpatterns += yasg_schema.urls