from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Post
from django.db.models import Q
from .forms import PostCreateForm

class AboutPageView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('posts:home')
    # fields = ['user','title', 'content']



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
        super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            object_list = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        else:
            object_list = None
        return object_list