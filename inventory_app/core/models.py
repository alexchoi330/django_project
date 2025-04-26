from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=500)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=500)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    #category is a one to many relationship with product, if category is deleted then all products connected to it are also deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # tag is a many to many relationship with product
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.name