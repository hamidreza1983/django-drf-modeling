from rest_framework import viewsets
from .serializer import *
from ...models import *
from rest_framework.permissions import IsAuthenticated




class ServiceView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer
    queryset = Service.objects.filter(status=True)



class MenuView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.filter(status=True)



class EventsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Events
    queryset = Events.objects.filter(status=True)


class SkillsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Skills
    queryset = Skills.objects.all()




class ChefView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChefSerializer
    queryset = Chefs.objects.filter(status=True)


class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()