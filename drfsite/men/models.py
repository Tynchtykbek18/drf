from django.contrib.auth.models import User
from django.db import models


class Men(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    content = models.TextField(max_length=5000, default='')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    cat = models.IntegerField(default=1)

    def __str__(self):
        return self.cat