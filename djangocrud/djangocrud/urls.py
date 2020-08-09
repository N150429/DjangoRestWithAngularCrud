from django.contrib import admin
from django.urls import path,include
from api.views import MovieViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movies',MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
