from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse



# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural='Categories'

    def get_absolute_url(self):
        return reverse('store:product_category', args=[self.slug])
        
    def __str__(self):
        return self.category_name



class Tags(models.Model):
    tag_name=models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural='Tags'


    def __str__(self):
        return self.tag_name




class Product (models.Model):
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    tag_name=models.ForeignKey(Tags,related_name='product',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    slug=models.SlugField()
    short_description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    featured_image= models.ImageField(upload_to='images/')
    other_image1= models.ImageField(upload_to='images/', blank=True, null=True)
    other_image2= models.ImageField(upload_to='images/',blank=True,null=True)
    other_image3= models.ImageField(upload_to='images/',blank=True,null=True)
    price = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    is_active =  models.BooleanField(default=True)
    created= models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Product'
        verbose_name_plural='Products'

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    
    def __str__(self):
        return self.product_name
