from django.db import models
from authapp.models import User

# Create your models here.
class ChatGroup(models.Model):
    group_name = models.Charfield(max_length=10000, unique=True)

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = "ChatGroup"
        verbose_name_plural = "ChatGroups"

class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.Charfield(max_length=500)
    created = models.DateTimeFielsd(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} : {self.body}'

    class Meta:
        ordering = ['-created']
