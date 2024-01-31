from rest_framework import viewsets
from .serializer import *
from ...models import *
from rest_framework.permissions import IsAuthenticated

class ChefView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChefSerializer
    queryset = Chef.objects.filter(status=True)

class PartyView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Party
    queryset = Party.objects.filter(status=True)

class ServiceView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer
    queryset = Service.objects.filter(status=True)

class FoodView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FoodSerializer
    queryset = Food.objects.filter(status=True)


class SkillsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Skill
    queryset = Skill.objects.all()


class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()