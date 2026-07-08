from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    
    def __str__(self):
        return self.title 
    
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    nop = models.IntegerField(default=0)
    isbn = models.CharField(max_length=200)
    publish_year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to="books/")
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, default="N/A")
    def __str__(self):
        return self.title
    

class Coupon(models.Model):
    code = models.CharField(max_length=200)
    discount = models.IntegerField()
    def __str__(self):
        return self.code
    
class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    area = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user_id.username
  
class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon_id = models.ForeignKey(Coupon, on_delete=models.CASCADE,null=True, blank=True)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE,null=True, blank=True)
    is_ordered = models.BooleanField(default=False)
  
class OrderItem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    is_ordered = models.BooleanField(default=False)
    
    