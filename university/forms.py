from django import forms
from .models import Teacher, Student, Class


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone_number', 'email']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'subject']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['students', 'teacher', 'title']