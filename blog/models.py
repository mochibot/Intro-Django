from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalBlog(Blog):
    author = models.ForeignKey(User, on_delete=models.CASCADE)