from django.urls import path,include
from .views import *


app_name = 'accounts'


urlpatterns = [
    path('api/V1/', include('accounts.api.V1.urls')),
]