from django.urls import include, path
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users-auth/',
         include('rest_framework.urls', namespace='rest_framework')),
    path('', include('data_api.urls'))
]
