from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('posts:home')
    fields = ['user','title', 'content']



class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ['title', 'content']




class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts:home')


class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_search.html'

    def get_queryset(self):
        result = super(PostSearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            object_list = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        else:
            object_list = None
        return object_list