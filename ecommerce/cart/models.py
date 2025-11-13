from django.db import models
from django.db.models.fields import DateTimeField
from shop.models import Product
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def subtotal(self):
        return self.product.price * self.quantity



class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.IntegerField(null=True)
    order_id=models.CharField(max_length=30,null=True)
    phone = models.IntegerField()
    address=models.TextField()
    payment_method = models.CharField(max_length=30)
    ordered_date = models.DateTimeField(auto_now_add=True)
    is_ordered=models.BooleanField(default=False)
    delivery_status=models.CharField(default="pending")
    def __str__(self):
        return self.user.username


class Order_items(models.Model):
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='products')
     quantity=models.IntegerField()
     def __str__(self):
         return self.product.name