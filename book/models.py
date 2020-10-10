from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    IBN = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title