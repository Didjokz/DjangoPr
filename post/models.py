import uuid
from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=50)
    text = models.TextField()