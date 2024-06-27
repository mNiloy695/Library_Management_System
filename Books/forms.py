from typing import Any
from django import forms
from .models import Review,Borrow
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['body','rating']

