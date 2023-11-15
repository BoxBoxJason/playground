from django import forms
from taverne.models import Character

class MoveForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('lieu',)
