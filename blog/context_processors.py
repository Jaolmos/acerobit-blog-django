from .models import Category, Tag
from django.db.models import Count

def sidebar_context(request):
    """
    Context processor para añadir categorías y tags al sidebar.
    Disponible en todos los templates automáticamente.
    """
    return {
        'categories': Category.objects.annotate(
            post_count=Count('posts')
        ).order_by('-post_count')[:10],  # Top 10 categorías con más posts
        
        'tags': Tag.objects.annotate(
            post_count=Count('posts')
        ).order_by('-post_count')[:10]  # Top 10 tags más usados
    }