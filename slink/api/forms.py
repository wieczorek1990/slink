from django import forms

from api import validators


class LinkForm(forms.Form):
    link = forms.CharField(label='Link', max_length=2048,
                           validators=validators.URL_VALIDATORS)
