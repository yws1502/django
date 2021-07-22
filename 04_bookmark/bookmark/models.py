from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField(verbose_name='Site URL')
    def __str__(self):
        return '이름 : {0}, 주소 : {1}'.format(self.site_name, self.url)

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])