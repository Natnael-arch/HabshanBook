from django.contrib import admin
from .models import Book, Cart, Purchase, Customer, BookItems
# Register your models here.
admin.site.register(Purchase)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(BookItems)