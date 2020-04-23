from django.forms  import ModelForm
from Webapp.models import Religion
from django import forms
class ReligionForm(ModelForm):
    class Meta:
        model=Religion
        fields='__all__'
class InputForm(forms.Form):
    bars=forms.IntegerField()
    stripes=forms.IntegerField()
    colours=forms.IntegerField()
    red=forms.IntegerField()
    green=forms.IntegerField()
    blue=forms.IntegerField()
    gold=forms.IntegerField()
    white=forms.IntegerField()
    black=forms.IntegerField()
    orange=forms.IntegerField()
    circles=forms.IntegerField()
    crosses=forms.IntegerField()
    saltires=forms.IntegerField()
    quarters=forms.IntegerField()
    sunstars=forms.IntegerField()
    crescent=forms.IntegerField()
    triangle=forms.IntegerField()
    icon=forms.IntegerField()
    animate=forms.IntegerField()
    text=forms.IntegerField()
   