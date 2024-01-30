from django.urls import path
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



app_name = 'api-v1-accounts'


urlpatterns = [
    path('registrations', ReigsterApiView.as_view(), name = 'registrations'),
    path('token/login/', CustomAuthToken.as_view(), name = 'token-login'),
    path('token/logout/', CustomDestroyAuthToken.as_view(), name = 'token-logout'),
    path('token/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]