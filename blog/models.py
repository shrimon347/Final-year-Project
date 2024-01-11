from django.db import models
import uuid
from ckeditor.fields import RichTextField
from base.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    slug = models.SlugField() 

    def __str__(self):
        return self.title
    
class Post(models.Model) :
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='blog-img')
    content = RichTextField()
    post_id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=500)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['-created', '-modified']

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.comment[0:50]