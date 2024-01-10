from django import forms

class emailForm(forms.Form):
    email = forms.EmailField(label='Okay, so can you please put your email address in here ???')