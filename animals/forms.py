from django import forms
from animals.models import Animals


class AnimalsForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = '__all__'
