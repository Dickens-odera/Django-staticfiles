from django import forms

class FeedbackForm(forms.Form):
	username = forms.CharField(max_length = 200, required = True)
	email = forms.EmailField()
	comment = forms.CharField(widget = forms.Textarea)
	
