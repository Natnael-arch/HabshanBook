import django_filters
from .models import *
from django_filters import CharFilter


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title']
        title = CharFilter(field_name='title', lookup_expr='icontains')
