from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# We want an Article model, that has the following fields:
# title, body, date, author(key)
# For date, we want to use models.DateTimeField(auto_now_add=True)
# CharField -> This allows us to set a max_length; Set the maximum length to 255

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])