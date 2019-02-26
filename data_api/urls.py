from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from data_api import views

urlpatterns = [
    path('hits/', views.HitList.as_view()),
    path('hit/<int:pk>', views.HitDetail.as_view(), name='hit-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
