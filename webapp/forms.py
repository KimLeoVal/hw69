from django import forms

from webapp.models import Test


class TestForm(forms.ModelForm):
    class Meta:
        model=Test
        fields='__all__'
