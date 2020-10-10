from django.urls import path
from .views import BookListView, detail_category
urlpatterns = [
    path('', BookListView.as_view(), name='home_list'),
    path('category/<str:cats>/',detail_category, name='category')
]