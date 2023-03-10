from django.db import models
import random
from django.utils import timezone
from django.utils.translation import gettext as _
from products.models import Product
# Create your models here.

# توليد كود عشوائي طولو 8 

def generate_code(length=8):
    numbers='0123456789'
    return ''.join(random.choice(numbers) for _ in range(length))
STATUS_CHOICES = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)
class Order(models.Model):
    code = models.CharField(_('Code'),max_length=8,default=generate_code)
    order_status = models.CharField(_('Order Status'),max_length=20,choices=STATUS_CHOICES)
    order_time = models.DateTimeField(_('Order Time'),default=timezone.now)
    delivery_time =models.DateTimeField(_("Delivery Time"),null=True,blank=True)
    def __str__(self):
        return self.code

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete = models.CASCADE,verbose_name=_('Order'))
    product = models.ForeignKey(Product,related_name='order_product',verbose_name=_('Product'),on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.FloatField(_('Quantity'))
    price = models.FloatField(_('Price'))
    def __str__(self):
        return str(self.order)