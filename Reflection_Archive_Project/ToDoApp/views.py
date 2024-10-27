from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from RA_Register_App.models import RA_RegistrationModel
from .models import todo_model
from .forms import Todo_Form
from django.contrib import messages

def todo_page(request, user_id):
    user = get_object_or_404(RA_RegistrationModel, id=user_id)
    user_name = f"{user.first_name} {user.last_name}"

    todos_list = todo_model.objects.filter(user=user, status='To Do')
    in_progress_list = todo_model.objects.filter(user=user, status='In Progress')
    completed_list = todo_model.objects.filter(user=user, status='Completed')

    paginator_todos = Paginator(todos_list, 6)
    page_number = request.GET.get('page')
    todos_page = paginator_todos.get_page(page_number)

    paginator_in_progress = Paginator(in_progress_list, 6)
    in_progress_page_number = request.GET.get('in_progress_page')
    in_progress_page = paginator_in_progress.get_page(in_progress_page_number)

    paginator_completed = Paginator(completed_list, 6)
    completed_page_number = request.GET.get('completed_page')
    completed_page = paginator_completed.get_page(completed_page_number)

    if request.method == 'POST':
        if 'add_todo' in request.POST:
            todo_text = request.POST.get('todo_text')
            if todo_text:
                new_todo = todo_model(user=user, todo=todo_text, status='To Do')
                new_todo.save()
                messages.success(request, 'Todo added successfully')
                return redirect('todo_page', user_id=user.id)

        elif 'edit_todo' in request.POST:
            todo_id = request.POST.get('todo_id')
            todo_item = get_object_or_404(todo_model, id=todo_id, user=user)
            request.session['editing_todo_id'] = todo_item.id
            request.session['editing_todo_text'] = todo_item.todo
            return redirect('todo_page', user_id=user.id)

        elif 'save_todo' in request.POST:
            todo_id = request.POST.get('todo_id')
            todo_text = request.POST.get('todo_text')
            if todo_id and todo_text:
                todo_item = get_object_or_404(todo_model, id=todo_id, user=user)
                todo_item.todo = todo_text
                todo_item.save()
                del request.session['editing_todo_id']
                del request.session['editing_todo_text']
                messages.success(request, 'Todo updated successfully')
                return redirect('todo_page', user_id=user.id)

        elif 'mark_in_progress' in request.POST:
            todo_id = request.POST.get('todo_id')
            if todo_id:
                todo_item = get_object_or_404(todo_model, id=todo_id, user=user)
                todo_item.status = 'In Progress'
                todo_item.save()
                messages.success(request, 'Todo status updated to In Progress')
                return redirect('todo_page', user_id=user.id)

        elif 'complete_task' in request.POST:
            todo_id = request.POST.get('todo_id')
            if todo_id:
                todo_item = get_object_or_404(todo_model, id=todo_id, user=user)
                todo_item.status = 'Completed'
                todo_item.save()
                messages.success(request, 'Todo marked as completed')
                return redirect('todo_page', user_id=user.id)

        elif 'delete_todo' in request.POST:
            todo_id = request.POST.get('todo_id')
            if todo_id:
                todo_item = get_object_or_404(todo_model, id=todo_id, user=user)
                todo_item.delete()
                messages.success(request, 'Todo deleted successfully')
                return redirect('todo_page', user_id=user.id)

    return render(request, 'todo.html', {
        'user': user,
        'user_name': user_name,
        'form': Todo_Form(),
        'todos': todos_page,
        'in_progress_tasks': in_progress_page,
        'completed_tasks': completed_page,
        'editing_todo_id': request.session.get('editing_todo_id'),
        'editing_todo_text': request.session.get('editing_todo_text'),
    })
