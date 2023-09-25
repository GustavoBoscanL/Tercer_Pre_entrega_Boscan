from django import forms
from .models import User, Employees, Washing_prices


class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
       
class employees_form(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'

class washing_price_form(forms.ModelForm):
    class Meta:
        model = Washing_prices
        fields = '__all__'