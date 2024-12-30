from django.urls import path
from . import views

app_name = 'blog' 

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('category/<slug:slug>/', views.PostByCategoryView.as_view(), name='post_by_category'),
    path('tag/<slug:slug>/', views.PostByTagView.as_view(), name='post_by_tag'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]