



from django import forms
from django.forms import ValidationError
from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label='Not selected'
    class Meta:
        model=States
        fields=['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':'60', 'rows':10}),
            
        }
        
    def clean_title(self):
        title=self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError('Length of state\'s name is more than 200')
        return title