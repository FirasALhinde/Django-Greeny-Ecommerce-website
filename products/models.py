from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
FLAG_TYPE =(
    ('New','New'),
    ('Feature','Feature'),
)
class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    sku = models.IntegerField(_('Sku'))
    brand = models.ForeignKey('Brand',related_name='product_brand',verbose_name=_('Brand'),on_delete=models.SET_NULL,null=True,blank=True)
    price = models.FloatField(_('Price'))
    desc = models.TextField(_('Description'),max_length=10000)
    category = models.ForeignKey('Category',related_name='product_category',verbose_name=_('Category'),on_delete=models.SET_NULL,null=True,blank=True)
    tags = ''
    # weight =
    flag = models.CharField(_("Flag"),choices=FLAG_TYPE,max_length=10) 
    def __str__(self):
        return self.name

class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_image',verbose_name=_('Product'),on_delete=models.CASCADE)
    image = models.ImageField(_('Image'),upload_to='products/')
    def __str__(self):
        return str(self.product) 


class Brand(models.Model):
    name = models.CharField(_('Name'),max_length=50)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    image = models.ImageField(_('Image'),upload_to='categories/')
    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_user',verbose_name=_('User'),on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='review_product',verbose_name=_('Product'),on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(_('Review'),max_length=10000)
    rate = models.IntegerField(_('Rate'),
        validators=[MaxValueValidator(5), MinValueValidator(0)])
    created_at = models.DateTimeField(_('Created At'),default=timezone.now)
    def __str__(self):
        return f'{self.user.username} - {self.product.name}'

