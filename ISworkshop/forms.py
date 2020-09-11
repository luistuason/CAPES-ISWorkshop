from django import forms
from .models import ProfilePage
import datetime

class ProfilePageForm(forms.ModelForm):
    email = forms.EmailField(
        label = 'Email', 
        widget = forms.TextInput(attrs = {'placeholder': 'Email', 'class':'email form-control'}), 
        max_length = 60
    )

    student_number = forms.CharField(
        label = 'Student Number', 
        widget = forms.TextInput(attrs = {'placeholder': 'Student Number', 'class':'student_number form-control'}), 
        max_length = 9
    )

    first_name = forms.CharField(
        label = 'First Name', 
        widget = forms.TextInput(attrs = {'placeholder': 'First Name', 'class':'first_name form-control'}), 
        max_length = 60
    )

    last_name = forms.CharField(
        label = 'Last Name', 
        widget = forms.TextInput(attrs = {'placeholder': 'Last Name', 'class':'last_name form-control'}), 
        max_length = 60
    )
    graduation_year = forms.IntegerField(
        min_value = datetime.date.today().year,
        max_value = datetime.date.today().year + 10,
        label = 'Expected Year of Graduation', 
        widget = forms.NumberInput(attrs = {'class':'graduation_year form-control'}),
    )
    
    degree = forms.ChoiceField(
        choices= ProfilePage.DEGREES,
        label = 'Degree',
        widget = forms.Select(attrs = {'class':'degree form-control'})
    )

    program = forms.ChoiceField(
        choices= ProfilePage.PROGRAMS,
        widget = forms.Select(attrs = {'class':'program form-control'})
    )
    class Meta:
        model = ProfilePage
        fields = ('email', 'student_number', 'first_name', 'last_name', 'graduation_year', 'degree', 'program', 'profile_picture',)