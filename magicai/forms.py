from django import forms

from magicai.models import UserPrompt


class UserPromptForm(forms.ModelForm):

    class Meta:
        model = UserPrompt
        fields = ["prompt"]
