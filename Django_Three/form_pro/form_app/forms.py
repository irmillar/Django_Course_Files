from django import forms

class FormName(forms.Form):
    name = forms.CharField(max_length=264)
    email = forms.EmailField(max_length=264)
    text_area = forms.CharField(widget=forms.Textarea)
