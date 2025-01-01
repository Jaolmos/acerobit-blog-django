from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'slug': self.slug})
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'etiqueta'
        verbose_name_plural = 'etiquetas'

    def __str__(self):
        return self.name


class Post(models.Model):
   title = models.CharField(max_length=200)
   slug = models.SlugField(max_length=200, unique=True)
   content = HTMLField()
   created_at = models.DateTimeField(auto_now_add=True) 
   updated_at = models.DateTimeField(auto_now=True)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
   tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

   class Meta:
       ordering = ['-created_at']  
       verbose_name = 'entrada'
       verbose_name_plural = 'entradas'

   def __str__(self):
       return self.title

   def get_absolute_url(self):
       return reverse('blog:post_detail', kwargs={'slug': self.slug})
    
