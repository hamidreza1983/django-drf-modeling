from django.urls import path, include
from .views  import *

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('api/V1/', include('restaurant.api.V1.urls')),
]