from django import forms

class ContactForm(forms.form):
    email = forms.EmailField(
        required =True,
        widhget=forms.EmailInput(attrs={'placeholder':'Enter your email'})
    )
    message = forms.CharField(
        required=True
        widget=forms.Textarea(attrs={'placeholder':'Enter your message'}
    )
