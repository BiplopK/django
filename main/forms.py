from django import forms
from .models import Users, Family
class UserForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=[
            'first_name',
            'last_name',
            'phone',
            'date_joined'
        ]

class FamilyForm(forms.ModelForm):
    class Meta:
        model=Family
        fields=[
            'father',
            'mother',
            'family_name',
            'child'
            ]