from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter username"}), label=""
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter pasword"}), label=""
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_user_exists = User.objects.filter(username=username).exists()
        if not is_user_exists:
            raise forms.ValidationError("User do not exists")
        return username
