from genericpath import exists
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils.text import slugify
from ckeditor.fields import RichTextField
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    slug = models.SlugField(unique=True, max_length=255)
    published_date = models.DateTimeField(auto_now_add=True) 
    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'slug': self.slug})



# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by('-id')
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug




# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#     if instance.slug:
#         instance.slug = 
# pre_save.connect(pre_save_post_receiver, sender=Post)