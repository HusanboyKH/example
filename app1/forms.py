from django import  forms
from .models import TodoModel
class ToDoForms(forms.ModelForm):
    task_uz =forms.CharField()
    task_en = forms.CharField()

    note_uz =forms.CharField()
    note_en = forms.CharField()

    class Meta:
        model =TodoModel
        exclude=['task','note']