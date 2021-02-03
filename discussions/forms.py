from django import forms
from . import models


class AddCommentForm(forms.Form):

    message = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"placeholder": "Add a Comment"})
    )


class CreateDiscussionForm(forms.ModelForm):
    class Meta:
        model = models.Discussion
        fields = ("topic",)

    def save(self, *args, **kwargs):
        discussion = super().save(commit=False)
        return discussion