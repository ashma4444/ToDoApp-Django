from django import forms
from .models import ToDoLists

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoLists
        fields = ['task']
        widgets = {
            'task': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add new task ...'})
        }