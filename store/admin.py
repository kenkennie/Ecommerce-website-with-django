from django.contrib import admin
from . models import Product,Category,Tags
# Register your models here.
@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display= ['tag_name']
    prepopulated_fields={'slug':('tag_name',)}

@admin.register(Category)
class CategAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    prepopulated_fields={'slug':('category_name',)}

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display=['product_name','price', 'in_stock',]
    prepopulated_fields={'slug':('product_name',)}
    