from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'
router.register('menu', MenuView, basename='Menu')
router.register('Event', EventView, basename='Event')
router.register('Chefs', ChefsView, basename='Chefs')
router.register('Order', OrderView, basename='Order')
router.register('ContactUs', ContactUsView, basename='ContactUs')
router.register('category', CategoryView, basename='category')
router.register('skills', SkillsView, basename='skills')


urlpatterns = router.urls
