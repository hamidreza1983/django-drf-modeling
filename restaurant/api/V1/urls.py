from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

app_name = 'api-v1'


urlpatterns = [
    path("courses/",CourseView.as_view({'get': 'list', 'post':'create'}),name='courses'),
    path("courses/<int:pk>/",CourseView.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}),name='course-detail'),

]