from django.urls import include, path
from rest_framework import routers
from users import views

from data_api.views import HitViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'hits', HitViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'silk/', include('silk.urls', namespace='silk')),
    path(r'users-auth/',
         include('rest_framework.urls', namespace='rest_framework')),
]
