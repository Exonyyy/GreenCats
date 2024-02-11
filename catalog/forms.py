from django import forms
from models import *


class NewProtectionType(forms.ModelForm):

    class Meta:
        model = BankProtectionTypes
        fields = ['name']


class NeBankProtectionStructure(forms.ModelForm):

    class Meta:
        model = BankProtectionStructures
        fields = ['name', 'short_description', 'full_description', 'photo', 'mark', 'prognosis',
                  'type', 'build_date', 'last_repair_date', 'latitude', 'longitude']
