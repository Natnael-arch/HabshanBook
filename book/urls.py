from django.urls import path
from .views import BookListView, detail_category, add_cart
urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('category/<str:cats>/', detail_category, name='category'),
    path('carts', add_cart, name='cart')
]