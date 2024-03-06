import uuid
from django.db import models

class Person(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    # Добавьте остальные поля модели