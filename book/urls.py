from django.urls import path
from .views import BookListView, detail_category, BookDetailView, add_cart, cart
urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('category/<str:cats>/', detail_category, name='category'),
    path('carts/', cart, name='cart'),
    path('add_cart/', add_cart, name='add_cart'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail')
    
]