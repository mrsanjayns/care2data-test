from django import forms
from .models import Student  # Updated import

class StudentForm(forms.ModelForm):  # Updated form name
    class Meta:
        model = Student  # Updated model reference
        fields = ['study_name', 'study_description', 'study_phase', 'sponsor_name']  # Updated field names
