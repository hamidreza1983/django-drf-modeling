from .serializer import *
from ...models import *
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly




class FoodView(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.filter(status=True)
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['category', 'title']
    search_fields = ['content', 'category__name', 'chiefs__info__email']
    ordering_fields = ['created_date']



class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SkillsView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()


class CheifView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = ChiefSerializer
    queryset = Chief.objects.filter(status=True)


class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = ContactUs.objects.all()


class ServiceView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ServiceSerializer
    queryset = Services.objects.all()


class eventView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ServiceSerializer
    queryset = Services.objects.all()
class eventView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ServiceSerializer
    queryset = Services.objects.all()
