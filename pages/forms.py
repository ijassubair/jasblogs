from django import forms
from pages.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = '__all__'
        widgets = {
            'article_ready': forms.RadioSelect()
        }
