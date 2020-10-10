from django.shortcuts import render
from .models import Category, Book
from django.views.generic import ListView

from django.views.generic import DetailView

# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'object_list'


def detail_category(request, cats):
    cat_101 = Book.objects.filter(category=cats)
    context = {
        'cate': cat_101
    }
    return render(request, 'category.html', context)
