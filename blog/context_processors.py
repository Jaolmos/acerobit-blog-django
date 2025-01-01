from .models import Category, Tag

def sidebar_context(request):
    """
    Context processor para añadir categorías y tags al sidebar.
    Disponible en todos los templates automáticamente.
    """
    return {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all()
    }