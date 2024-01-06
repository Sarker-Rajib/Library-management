from django import forms
from .models import Review

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ['name', 'body']
        widgets= {
          'body': forms.Textarea(attrs={'rows': 4})
        }