from unicodedata import name
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/detail/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<slug:slug>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<slug:slug>', PostDeleteView.as_view(), name='post_delete'),   

]