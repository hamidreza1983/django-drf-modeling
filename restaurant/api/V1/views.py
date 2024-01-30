from rest_framework.permissions import IsAuthenticated
from .serializer import *
from ...models import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter







class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(status=True)
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['category', 'title']
    search_fields = ['content', 'category__name', 'teacher__info__email']
    ordering_fields = ['created_date']
    pagination_class = CustomePaginate



class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SkillsView(viewsets.ModelViewSet):
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()


class TrainerView(viewsets.ModelViewSet):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.filter(status=True)