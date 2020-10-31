from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse_lazy, reverse


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


class Book(models.Model):
    CATEGORY = (
        ('Amharic', 'Amharic'),
        ('English', 'English'),
        ('Comedy', 'Comedy')
    )
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    IBN = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=50, null=True, blank=True,choices=CATEGORY)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.DecimalField(blank=False, null=False, default=0.0, max_digits=10000, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def cart_total(self):
        bookitems = self.bookitems_set.all()
        total = sum([item.get_total for item in bookitems])
        return total

    @property
    def cart_item(self):
        bookitems = self.bookitems_set.all()
        total = sum([item.quantity for item in bookitems])
        return total


class BookItems(models.Model):
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.SET_NULL)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        total = self.book.price * self.quantity
        return total

    def __str__(self):
        return str(self.book.title)


class Purchase(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField(null=True, blank=False)

    def __str__(self):
        return str(self.address)