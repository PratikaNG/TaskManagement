from django import forms
from .models import TaskDB


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskDB
        fields = ['task','priority']
