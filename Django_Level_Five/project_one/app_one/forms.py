from django import forms
from app_one.models import UserProfileInfo

class UserProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta():
        model = UserProfileInfo
        exclude('user',)
