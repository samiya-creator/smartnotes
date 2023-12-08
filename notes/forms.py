from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-5'}),
            'content': forms.Textarea(attrs={'class':'form-control my-5'}),
        }
        labels = {
        'content':'Write your note here'
        }
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long")
        # if "django" not in title.lower():
        #     raise forms.ValidationError("Title must contain django")
        return title