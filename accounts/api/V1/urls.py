from django.urls import path
from .views import *



app_name = 'api-v1-accounts'


urlpatterns = [
    path('registrations', ReigsterApiView.as_view(), name = 'registrations'),
    path('token/login/', CustomAuthToken.as_view(), name = 'token-login'),
    path('token/logout/', CustomDestroyAuthToken.as_view(), name = 'token-logout'),


]