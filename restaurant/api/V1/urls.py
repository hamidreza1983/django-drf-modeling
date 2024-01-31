from django.urls import path
from .views import *

app_name = 'api-v1'


urlpatterns = [
    path("foods/",FoodView.as_view({'get': 'list', 'post':'create'}),name='foods'),
    path("foods<int:pk>/",FoodView.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}),name='food-detail'),

    path("chief/",CheifView.as_view({'get': 'list', 'post':'create'}),name='chiefs'),
    path("chief<int:pk>/",CheifView.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}),name='chief-detail'),

    path("services/",ServiceView.as_view({'get': 'list','post':'create', }),name='services'),
    path("services/<int:pk>",ServiceView.as_view({'put':'update','delete': 'destroy'}),name='service-edit'),

    path("events/",eventView.as_view({'get': 'list','post':'create', }),name='events'),
    path("events/<int:pk>",eventView.as_view({'put':'update','delete': 'destroy'}),name='event-edit'),
    
    path("contact/",ContactView.as_view({'post':'create'}),name='contactus'),

    path("skill/",SkillsView.as_view({'get': 'list','post':'create'}),name='skills'),


]