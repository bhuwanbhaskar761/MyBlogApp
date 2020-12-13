from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    image = models.FileField(null=True)
    mode = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username + "(" + self.title + ")"

