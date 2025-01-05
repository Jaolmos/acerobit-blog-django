from django.urls import path
from . import views

app_name = 'blog' 

urlpatterns = [
    # Páginas legales y de contacto
    path('aviso-legal/', views.aviso_legal, name='aviso-legal'),
    path('privacidad/', views.politica_privacidad, name='privacidad'),
    path('cookies/', views.politica_cookies, name='cookies'),
    path('contact/', views.contact, name='contact'),
    
    # Rutas del blog
    path('', views.PostListView.as_view(), name='post_list'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('category/<slug:slug>/', views.PostByCategoryView.as_view(), name='post_by_category'),
    path('tag/<slug:slug>/', views.PostByTagView.as_view(), name='post_by_tag'),
    path('categories/', views.CategoriesListView.as_view(), name='categories_list'),
    path('tags/', views.TagsListView.as_view(), name='tags_list'),
    
    # Esta URL debe ir al final porque captura cualquier slug
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    
       
]