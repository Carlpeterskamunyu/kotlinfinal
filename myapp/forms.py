from django import forms
from myapp.models import Appointments

class AppointmentsForm(forms.ModelForm):  # Corrected the name to ModelForm
    class Meta:
        model = Appointments
        fields = '__all__'
