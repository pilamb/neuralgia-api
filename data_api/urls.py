from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from data_api import views

urlpatterns = [
    path('hits/', views.hits_list),
    path('hit/<int:pk>', views.hit_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
