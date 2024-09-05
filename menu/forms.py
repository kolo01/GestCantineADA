

from django import forms

from menu.models import MenuModel


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuModel 
        fields = ('dishes',)
        