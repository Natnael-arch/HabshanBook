from django.urls import path
from .views import book_list_view,\
    detail_category, purchase, BookDetailView,\
    add_cart, cart, about_us, delete_cart
urlpatterns = [
    path('', book_list_view, name='home'),
    path('category/<str:cats>/', detail_category, name='category'),
    path('carts/', cart, name='cart'),
    path('add_cart/', add_cart, name='add_cart'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('purchase', purchase, name='purchase'),
    path('about', about_us, name="about"),
    path('delete_cart/',delete_cart, name="delete_cart")

]