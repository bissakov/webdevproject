from django.db import models

from django.contrib.auth.models import User

class Consumer(User):
    name = models.CharField(max_length=250,default='')
    phone = models.CharField(max_length=250,default='')
    address = models.TextField(default = '')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'

class Category(models.Model):
    name = models.CharField(max_length=250,default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=250,default='')
    description = models.TextField(max_length=500,default='')
    image = models.ImageField(upload_to='assets',null=True,blank=True)
    price = models.DecimalField(max_digits=9,decimal_places=2,default=0)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return '%s (%s)' % (self.name, self.category)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Order(models.Model):
    consumer = models.ForeignKey(Consumer,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class OrderProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    ammount = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProducts'
