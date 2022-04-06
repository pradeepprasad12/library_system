from django import forms
from .models import Post




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'Book_Name'}
        labels = {'Book_Name':'Book_Name'}
        widgets = {
            'Book_Name': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
