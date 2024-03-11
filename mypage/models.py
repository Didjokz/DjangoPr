import uuid
from django.db import models

class Person(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(default="Test",max_length=50)
    is_active = models.BooleanField(default=True)
    
    # Добавьте остальные поля модели