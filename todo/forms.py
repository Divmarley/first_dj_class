from django import forms

from todo.models import Todo

# Create your models here.
class CreateTodo(forms.ModelForm):
    class Meta:
        model = Todo
        fields =['name','description']