from django.db import models
from django.urls import reverse 
from django.shortcuts import get_object_or_404
from categories.models import Category

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    no_of_page = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    # image = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='products/images', null=True, blank=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True
                                , related_name="allproducts")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    @property
    def show_url(self):
        return reverse('books.show', args=[self.id])
    
    @property
    def delete_url(self):
        return reverse('books.delete',args=[self.id])
    
    @property
    def update_url(self):
        return reverse('books.update',args=[self.id])
    
    @property
    def image_url(self):
        return f"/media/{self.image}"
    
    @classmethod
    def get_book_by_id(cls,id):
        return get_object_or_404(cls,pk=id)
    
    
    
    


