from django import forms

class SearchProfileForm(forms.Form):
    user_name = forms.CharField(max_length=150)
    

