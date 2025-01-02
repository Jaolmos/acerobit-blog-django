from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Category, Tag

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
        
    def location(self, obj):
        return obj.get_absolute_url()

class CategorySitemap(Sitemap):
    changefreq = "monthly"  
    priority = 0.6         

    def items(self):
        return Category.objects.all()
        
    def location(self, obj):
        return reverse('blog:post_by_category', args=[obj.slug])

class TagSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Tag.objects.all()
        
    def location(self, obj):
        return reverse('blog:post_by_tag', args=[obj.slug])