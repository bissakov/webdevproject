from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password = None):
#         if not email:
#             raise ValueError('Email is required.')
#         if not username:
#             raise ValueError('Username is required.')
#         user = self.model(
#             email = self.normalize_email(email),
#             username = username,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email = self.normalize_email(email),
#             password = password,
#             username = username,
#         )
#         is_admin = True
#         is_staff = True
#         is_superuser = True
#         user.save(using=self._db)

# class Account(AbstractBaseUser):
#     email = models.EmailField(verbose_name='email', max_length=60, unique=True)
#     email = models.CharField(max_length=30,unique=True)
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username',]

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self,perm,obj=None):
#         return self.is_admin
    
#     def has_module_perms(self, app_label):
#         return True

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
    id = models.IntegerField(primary_key=True)
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
    amount = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProducts'
