from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    # status = ChoiceFilter(choices=STATUS_CHOICES)
    class Meta:
        model = Category
        fields = ['name', 'status']
