
from .views import HelloViewSet

from django.urls import path

hello_world = HelloViewSet.as_view({'get': 'list'})

urlpatterns = [
    path(r'', hello_world),
]