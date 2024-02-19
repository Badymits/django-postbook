from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title               = models.CharField(max_length=255)
    body                = models.CharField(max_length=955, null=True, blank=True)
    date_posted         = models.DateTimeField(auto_now_add=True)
    image               = models.ImageField(upload_to='images', blank=True, null=True)
    slug                = models.SlugField(default="", max_length=255, blank=True, null=True)
    likes               = models.PositiveIntegerField(blank=True, default=0, null=True)
    dislikes            = models.PositiveIntegerField(blank=True, default=0, null=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
class Comment(models.Model):
    
    main_post           = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply               = models.ForeignKey('Comment', on_delete=models.DO_NOTHING, null=True, related_name='replies') # to be used in a nested comment thread
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body                = models.CharField(max_length=955)
    image               = models.ImageField(default='images', blank=True, null=True)
    likes               = models.PositiveIntegerField(blank=True, default=0, null=True)
    dislikes            = models.PositiveIntegerField(blank=True, default=0, null=True)
    date_posted         = models.DateTimeField(auto_now_add=True, null=True)
    comment_level       = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.first_name} replying to {self.main_post.title} content: {self.body}'
    
    # By making use of reply_id, we avoid loading the reply model object if it exists, which can lead to an N+1 problem
    @property
    def is_reply(self):
        return self.reply_id is not None
    
    # if true, then we can identify if it is a nested comment or not.
    @property
    def has_replies(self):
        return self.replies.exists()
    
    # gets all replies related to the object that called it
    @property
    def get_replies(self):
        return self.replies.all()
    
# class LikeModel(models.Model):
    
#     pass

# class DislikeModel(models.Model):
    
#     pass
    
