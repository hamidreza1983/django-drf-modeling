from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('chef', ChefView, basename='chef')
router.register('events', PartyView, basename='events')
router.register('skills', SkillView, basename='skills')
router.register('menu', FoodView, basename='menu')
router.register('category', CategoryView, basename='category')
router.register('service', ServiceView, basename='service')

urlpatterns = router.urls