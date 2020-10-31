from django.shortcuts import render
from .models import Book, BookItems, Cart, Purchase
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
import json
from .filter import BookFilter
from .forms import PurchaseForm
# Create your views here.


def book_list_view(request):
    book = Book.objects.all()
    myfilter = BookFilter(request.GET, queryset=book)
    book = myfilter.qs
    context = {'object_list': book, 'myfilter': myfilter}
    return render(request, 'home.html', context)


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


def detail_category(request, cats):
    cat_101 = Book.objects.filter(category=cats)
    book = Book.objects.all()
    myfilter = BookFilter(request.GET, queryset=book)
    book = myfilter.qs
    context = {
        'cate': cat_101, 'object_list': book, 'myfilter': myfilter
    }

    return render(request, 'category.html', context)


@login_required(login_url='login')
def cart(request):

    the_customer = request.user
    cart, ordered = Cart.objects.get_or_create(customer=the_customer)
    books = cart.bookitems_set.all()
    item_num = cart.bookitems_set.all().count()
    #search
    book = Book.objects.all()
    myfilter = BookFilter(request.GET, queryset=book)
    book = myfilter.qs

    context = {'carts': books,
               'item_num': item_num,
               'cart_obj': cart, 'object_list': book, 'myfilter': myfilter}
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


def purchase(request):
    form = PurchaseForm()
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            user = request.user
            cart, ordered = Cart.objects.get_or_create(customer=user)
            purchase, order = Purchase.objects.get_or_create(customer=user,
                                                             cart=cart,
                                                             address=address,
                                                             city=city,
                                                             phone=phone)
            purchase.save()

    return render(request, 'purchase.html', {'form':form})