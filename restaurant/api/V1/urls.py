from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('service', ServiceView, basename='service')
router.register('menu', MenuView, basename='menu')
router.register('events', EventsView, basename='events')
router.register('chef', ChefView, basename='chef')
router.register('skills', SkillsView, basename='skills')
urlpatterns = router.urls
