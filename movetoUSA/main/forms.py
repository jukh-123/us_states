



from django import forms
from django.forms import ValidationError
from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label='Not selected'
    class Meta:
        model=States
        fields=['title', 'slug', 'content', 'jobs', 'salary', 'living_expenses', 'photo', 'is_published', 'cat']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':'60', 'rows':10}),
        }
        
    def clean_title(self):
        title=self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError('Length of state\'s name is more than 200')
        return title


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class FileFieldForm(forms.Form):
    file_field = MultipleFileField()