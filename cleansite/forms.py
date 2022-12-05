from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label = 'Ваше имя',
        min_length = 3,
        widget=forms.TextInput(
        attrs = {'autocomplete':"off"}
    )
    )
    
    number = forms.CharField(
            label = 'Телефон',
            widget=forms.TextInput(
            attrs = {'autocomplete':"off"}
    )
    )
    