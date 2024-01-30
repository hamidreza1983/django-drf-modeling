from django.urls import path
from .views import *

app_name = 'api-v1'


urlpatterns = [
    path("foods/",FoodView.as_view({'get': 'list', 'post':'create'}),name='foods'),
    path("foods<int:pk>/",FoodView.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}),name='food-detail'),

    path("chief/",CheifView.as_view({'get': 'list', 'post':'create'}),name='chiefs'),
    path("chief<int:pk>/",CheifView.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}),name='chief-detail'),

    path("services/",ServiceView.as_view({'get': 'list','post':'create', 'put':'update','delete': 'destroy'}),name='services'),
    
    path("contact/",ContactView.as_view({'post':'create'}),name='contactus'),
]