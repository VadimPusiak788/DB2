from django.db import models


class ChatModel(models.Model):
    author_email = models.EmailField()
    text = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author_email

