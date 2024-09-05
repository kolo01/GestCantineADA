from django import forms

from dishes.models import DishesModel


class DishesForm(forms.ModelForm):
    class Meta:
        model = DishesModel
        fields = ('name','summary')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
        }