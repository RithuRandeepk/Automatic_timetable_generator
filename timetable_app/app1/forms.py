from django import forms
from .models import Course, Period, Staff, Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name','code']

class CourseForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),  
        widget=forms.CheckboxSelectMultiple,  
        required=True  
    )

    class Meta:
        model = Course
        fields = ['course_name', 'subjects']

class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ['session_name', 'start_time', 'end_time']
        
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'subjects']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple(),
        }