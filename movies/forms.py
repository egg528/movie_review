from django import forms
from . import models


class MovieSearchForm(forms.Form):
    search_word = forms.CharField(label="Movie Name")