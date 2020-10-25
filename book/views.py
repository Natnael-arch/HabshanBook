from django.shortcuts import render
from .models import Book, BookItems, Cart
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.http import JsonResponse
import json
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'object_list'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


def detail_category(request, cats):
    cat_101 = Book.objects.filter(category=cats)
    context = {
        'cate': cat_101
    }
    return render(request, 'category.html', context)


@login_required(login_url='login')
def cart(request):
    the_list = []
    books = BookItems.objects.all()
    cart_num = books.count()
    context = {'carts': books, 'cart_num': cart_num}
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def add_cart(request):
    data = json.loads(request.body)
    bookId = data['bookId']
    action = data['action']
    the_book = Book.objects.get(id=bookId)
    the_customer = request.user
    cart, ordered = Cart.objects.get_or_create(customer=the_customer)

    books, ordered = BookItems.objects.get_or_create(book=the_book, cart=cart)

    if action == "add":
        books.quantity = (books.quantity+1)

    elif action == "remove":
        books.quantity = (books.quantity-1)
    books.save()

    if books.quantity <= 0:
        books.delete()

    return JsonResponse('data add', safe=False)

