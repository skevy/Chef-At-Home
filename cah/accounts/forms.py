from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=30)
    email_address = forms.EmailField(max_length=255)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_email_address(self):
        email_address = self.cleaned_data.get("email_address", "")
        other_users = User.objects.filter(email=email_address)
        if other_users.count() > 0:
            raise forms.ValidationError("Duplicate email address!")
        return email_address

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2