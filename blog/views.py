from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from django.db.models import Q, Count
from django.shortcuts import render

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostByCategoryView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['slug']
        return context

class PostByTagView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['slug']
        return context

class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |          
                Q(content__icontains=query) |        
                Q(category__name__icontains=query) | 
                Q(tags__name__icontains=query)       
            ).distinct()                             
        return Post.objects.none()
    
class CategoriesListView(ListView):
    model = Category
    template_name = 'blog/categories_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.annotate(
            post_count=Count('posts')
        ).order_by('-post_count')  # Ordenar por número de posts

class TagsListView(ListView):
    model = Tag
    template_name = 'blog/tags_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.annotate(
            post_count=Count('posts')
        ).order_by('-post_count')  # Ordenar por número de posts
        

def aviso_legal(request):
    return render(request, 'blog/legal/aviso-legal.html')

def politica_privacidad(request):
    return render(request, 'blog/legal/privacidad.html')

def politica_cookies(request):
    return render(request, 'blog/legal/cookies.html')