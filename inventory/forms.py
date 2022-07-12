from django import forms
from .models import *
from inventory.models import Desktop, Laptop, Mobile


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ("type", "price", "status", "issues")


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ("type", "price", "status", "issues")


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ("type", "price", "status", "issues")
