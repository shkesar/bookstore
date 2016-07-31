from django import forms

from . import models

class Thread(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = models.Thread
        fields = ['text', 'document']

class Post(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = models.Post
        fields = ['text', 'document']
