from django.contrib import admin
from .models import Product,Category,ProductImages,Review,Brand
# Register your models here.

# لاضافة عدة صور ل ممنتج الواحد 
# يلي بدو ينعرض تحت 
class ProductImagesInline(admin.TabularInline):
    model = ProductImages 

# لح يتعرض
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]



admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImages)
admin.site.register(Review)
admin.site.register(Brand)


