from django import forms
from .models import (
    SensorsData,
    UserData,
    SensorsSetup
)


class SensorsDataForm(forms.ModelForm):
    class Meta:
        model = SensorsData
        fields = ('data', 'date_created', 'owner')


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ('data', 'date_created', 'owner')


class SensorsSetupForm(forms.ModelForm):
    class Meta:
        model = SensorsSetup
        fields = ('setup', 'date_created', 'owner')


