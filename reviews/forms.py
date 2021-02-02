from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    star = forms.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = models.Review
        fields = (
            "comment",
            "star",
        )
        widgets = {
            "comment": forms.TextInput(attrs={"placeholder": "Write Your Comment"}),
        }

    def save(self):
        review = super().save(commit=False)
        return review
