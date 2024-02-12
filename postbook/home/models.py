from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title               = models.CharField(max_length=255)
    body                = models.CharField(max_length=355)
    date_posted         = models.DateTimeField(auto_now_add=True)
    image               = models.ImageField(blank=True, null=True)
    slug                = models.SlugField(default="", max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
