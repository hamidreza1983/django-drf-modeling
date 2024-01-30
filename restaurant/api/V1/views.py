from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .serializer import *
from ...models import *
from rest_framework import viewsets




class FoodView(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['category', 'title']
    search_fields = ['content', 'category__name', 'chiefs__info__email']
    ordering_fields = ['created_date']



class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SkillsView(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()


class CheifView(viewsets.ModelViewSet):

    serializer_class = ChiefSerializer
    queryset = Chief.objects.filter(status=True)


class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = ContactUs.objects.all()


class ServiceView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Services.objects.all()
