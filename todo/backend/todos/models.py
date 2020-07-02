from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.title