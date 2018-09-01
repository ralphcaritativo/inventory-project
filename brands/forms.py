from django import forms
from .models import Brand


class BrandForm(forms.ModelForm):
    # status = ChoiceFilter(choices=STATUS_CHOICES)
    class Meta:
        model = Brand
        fields = ['name', 'status']
