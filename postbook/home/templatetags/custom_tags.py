from django import template
from django.shortcuts import get_object_or_404

from ..models import LikeModel, DislikeModel

register = template.Library()

@register.simple_tag
def is_liked(post, user):
    # its repetitive but this will still help
        
    try:
        post_filter = get_object_or_404(LikeModel, post=post)

        #print('post user likes: ', post_filter.users.filter(id=user.id).exists())
        if post_filter.users.filter(id=user.id).exists():
            return True
        
    except:
        
        return False 

@register.simple_tag
def is_disliked(post, user):
    
    try:
        post_filter = get_object_or_404(DislikeModel, post=post)

        #print('post user likes: ', post_filter.users.filter(id=user.id).exists())
        if post_filter.users.filter(id=user.id).exists():
            return True
        
    except:
        
        return False 

@register.simple_tag
def postVotes(*args):
    print(*args)
    pass