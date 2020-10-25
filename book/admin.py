from django.contrib import admin
from .models import Book, Cart, ShippingAddress, Customer, BookItems
# Register your models here.
admin.site.register(ShippingAddress)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(BookItems)