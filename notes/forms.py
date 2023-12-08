from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "django" not in title.lower():
            raise forms.ValidationError("Title must contain django")
        return title