from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Todo(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    date_completed=models.DateTimeField(blank=True,null=True)
    important=models.BooleanField(default=False)


    user=models.ForeignKey(User,on_delete=models.CASCADE)

    # 如果是on_delete = models.SET_NULL, null = True ，後面用username會報錯
    def __str__(self):
        return f'{self.id}-{self.title}({self.user.username})'