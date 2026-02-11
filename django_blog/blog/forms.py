from django import forms
from .models import Post,Tag
from .models import Comment
from taggit.forms import TagWidget

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
    """
    Form for creating and updating blog posts.
    The author field is excluded because it will be set automatically.
    """
    tags = forms.CharField(required=False, help_text="Separate tags with commas")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            'tags': TagWidget(),  
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']        