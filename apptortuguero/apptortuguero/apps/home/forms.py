from django import forms

class ContactForm(forms.Form):
	Nombre	= forms.EmailField(widget=forms.TextInput())
	Email	= forms.EmailField(widget=forms.TextInput())
	Asunto	= forms.CharField(widget=forms.TextInput())
	Texto	= forms.CharField(widget=forms.Textarea())