from django.contrib import admin
from .models import Post, Category, Tag

from django.contrib import admin
from .models import Category, Tag, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'has_image')
    list_filter = ('category', 'tags', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    
    # Método para mostrar si el post tiene imagen
    def has_image(self, obj):
        return bool(obj.featured_image)
    has_image.short_description = '¿Tiene imagen?'
    has_image.boolean = True
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

