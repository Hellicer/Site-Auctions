from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django.core.files.storage import FileSystemStorage
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField


fs = FileSystemStorage(location='/home/Hellicer/')


class User(AbstractUser):
    pass


class Category(models.Model):
    categorys = models.CharField(max_length=32)
    def __str__(self):
        return f"{self.categorys}"

class Card(models.Model):
    title = models.CharField(max_length=24, verbose_name="lot-input", blank=False,  default=None)
    description = models.TextField(max_length=300, blank=False,  default=None)
    comment = models.CharField(max_length=244, blank=True)
    price = models.FloatField(max_length=6, blank=False,  default=None,)
    pub_date = models.DateTimeField(
        'date published', auto_now_add=True, db_index=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lotAuthor", default=1)
    status_lot = models.BooleanField(default=1)
    winner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lotWinner", blank=True, null=True)
    close_date = models.DateTimeField('date closed', db_index=True, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    category = models.ManyToManyField(Category, blank=True, related_name="chooseCategory")
    checked =  models.BooleanField(default=0,)
    now_price = models.FloatField(max_length=6, blank=True, null=True,  default=None,)
    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    text = models.TextField(max_length=150,blank=False,  default=None,)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="usercom", default=1)
    pub_date = models.DateTimeField(
        'date published', auto_now_add=True, db_index=True)
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE, related_name="CardComment", default=1)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.text}"



class Rate(models.Model):
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE, related_name="RatePost", default=1)
    price = models.FloatField(max_length=6, blank=False,  default=None,)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="RateUser", default=1)
    pub_date = models.DateTimeField(
        'date published', auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.price}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Userwatchlist")
    title = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="CardWatchlist")
        
    def __str__(self):
        return f"{self.title}"