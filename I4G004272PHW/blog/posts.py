from django.db import posts
from django.contrib.auth.models import User

# Create your models here.
class Post(posts.Model):
    author = posts.ForeignKey(User, on_delete=posts.CASCADE)
    title = posts.CharField(max_length=200)
    text = posts.TextField()
    created_date = posts.DateTimeField(auto_now=True)
    published_date = posts.DateTimeField(auto_now_add=True)




