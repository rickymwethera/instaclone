from django import forms
from django.contrib.auth.models import User
from .models import Image, Comment, Profile


class PostForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Image 
  
        # specify fields to be used 
        fields = [ 
            "image", 
            "name",
            "caption", 
        ] 

class CommentForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Comment 
  
        # specify fields to be used 
        fields = [ 
            "comment", 
            
        ] 