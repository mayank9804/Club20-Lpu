from django import forms
from .models import ContactSection

class ContactForm(forms.ModelForm):
    class Meta:
        fields = ('name','email','message')
        model = ContactSection

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].label = 'Your Name'
        self.fields['email'].label = 'Your Email Address'
        self.fields['message'].label = 'Your Message'
