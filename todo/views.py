from django.shortcuts import render,redirect
from todo.forms import CreateTodo

from todo.models import Todo

# Create your views here.
def todo_view(request):
    template_name="todo.html"  
 
    if request.method =='POST':
        create_todo= CreateTodo(request.POST)
        if create_todo.is_valid():
            create_todo.save()
            return redirect('/todo')
    else:
        create_todo= CreateTodo()
    context={
        "todo_model_list":Todo.objects.all(),
        "create_todo_list":create_todo,
    }
    return render(request, template_name,context)



def delete_todo(request,id): 
    Todo.objects.get(id=id).delete()
    return redirect('todos:index')