from django.db import models
from django.conf import settings
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    book_product = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
     pass