from django import forms
from pgms_app.models import *

class form_register(forms.ModelForm):
    class Meta:
        model = model_register
        fields = ['uname','phone_number','address']
class form_rent(forms.ModelForm):
    class Meta:
        model = model_rent
        fields = ['uname','phone_number','amount']