from django import forms
from .models import MedicalRecord
from django.contrib.admin.widgets import AdminDateWidget
import datetime

class MedicalForm(forms.ModelForm):
    # timestamp = forms.DateField(label="Date", required=True, widget=forms.SelectDateWidget(), initial=datetime.date.today())
    class Meta:
        model = MedicalRecord
        widgets = {'timestamp': forms.DateInput(attrs={'type':'date'})}
        fields = ['timestamp', 'h2_plasma_glucose', 'fasting_plasma_glucose', 'hbA1c']
        labels = {'timestamp': 'Date', 'h2_plasma_glucose': '2-h plasma glucose', 'fasting_plasma_glucose': 'Fasting plasma glucose', 'hbA1c': 'hbA1c'}


# class MedicalForm(forms.Form):
#     timestamp = forms.DateField(label="Date", required=True, widget=forms.SelectDateWidget(), initial=datetime.date.today())
#     h2_plasma_glucose = forms.DecimalField(label="2-h plasma glucose", required=False, widget=forms.NumberInput(attrs={'placeholder':0.0}))
#     fasting_plasma_glucose = forms.DecimalField(label="Fasting plasma glucose",required=False, widget=forms.NumberInput(attrs={'placeholder':0.0}))
#     hbA1c = forms.DecimalField(label="hbA1c",required=False, widget=forms.NumberInput(attrs={'placeholder':0.0}))
