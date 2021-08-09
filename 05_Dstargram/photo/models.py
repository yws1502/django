from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

# ForeignKey
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # makemigrations -> migrate
    class Meta:
        ordering = ['-updated', ] # 정렬 기준

    def __str__(self):
        return self.author.username + ' ' + self.created.strftime('%Y-%m-%d %H:%M:%S')

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])