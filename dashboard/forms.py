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
