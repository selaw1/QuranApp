from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import UserBase


class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserBase
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
        help_texts = {"email": "IMPORTANT: this field can NOT be changed!"}

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username and UserBase.objects.filter(username__iexact=username).exists():
            self.add_error("username", "A user with that username already exists.")
        return cleaned_data


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = UserBase
        fields = ["email", "username", "first_name", "last_name"]

    def clean(self, **kwargs):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")

        if username and UserBase.objects.filter(username__iexact=username).exists():
            self.add_error("username", "A user with that username already exists.")
        return cleaned_data
