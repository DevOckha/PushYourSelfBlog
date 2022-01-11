from datetime import datetime
from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import Post
from .views import PostListView



class TestsView(TestCase):
   

    def setUp(self):
        self.user = User.objects.create(username='testuser123', password='testpass123')
        self.post = Post.objects.create(user=self.user, title='test', content='test content', slug='test', published_date=datetime.now())
    
        url = reverse('posts:home')
        self.response = self.client.get(url)

    def test_about_page_view(self):
        url = reverse('posts:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Page')
        self.assertNotContains(response, 'not in about page')
        self.assertTemplateUsed(response, 'blog/about.html')

    def test_detail_view(self):
        response = self.client.get(reverse('posts:post_detail', kwargs={'slug':self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_list_view(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'blog/home.html')
        self.assertContains(self.response, 'Posts')
        self.assertNotContains(self.response, 'hey i am not in home page!')

    def test_post_list_is_resolved(self):
        url = reverse('posts:home')
        self.assertEqual(resolve(url).func.view_class, PostListView)


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser123', password='testpass123')
        self.post = Post.objects.create(user=self.user, title='Test Title', content='test content', slug='test-title', published_date=datetime.now())
    
    def tearDown(self):
        self.user.delete()
    
    def test_str_is_equal_to_title(self):
        post = self.post
        self.assertEqual(str(post), self.post.title)

    def test_read_post(self):
        self.assertEqual(self.post.user, self.user)
        self.assertEqual(self.post.content, 'test content')
        self.assertEqual(self.post.slug, 'test-title')
    
    def test_update_post_content(self):
        self.post.content = 'new content'
        self.post.save()
        self.assertEqual(self.post.content, 'new content')
    
    def test_update_post_title(self):
        self.post.title = 'new title'
        self.post.save()
        self.assertEqual(self.post.title, 'new title')
        self.assertEqual(self.post.slug, 'new-title')
    
    def test_create_post(self):
        response = self.client.get(reverse('posts:post_detail', kwargs={'slug':self.post.slug}))
        self.assertEqual(self.post.title, 'Test Title')
        self.assertContains(response, 'test content')
        self.assertEqual(response.status_code, 200)
