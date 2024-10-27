from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from RA_Register_App.models import RA_RegistrationModel
from .models import todo_model
from .forms import Todo_Form
from django.contrib import messages

def todo_page(request, user_id):
    user = RA_RegistrationModel.objects.get(id=user_id)
    user_name = f"{user.first_name} {user.last_name}" if user else ""
    todos_list = todo_model.objects.filter(status='To Do')

    paginator = Paginator(todos_list, 6)
    
    # Get the page number from the query parameters
    page_number = request.GET.get('page', 1)

    # Ensure page number is a valid integer
    try:
        page_number = int(page_number)
        if page_number < 1:
            page_number = 1
    except ValueError:
        page_number = 1

    # Fetch todos for the current page
    try:
        todos = paginator.page(page_number)
    except EmptyPage:
        # If the page number is out of range, return the last page
        todos = paginator.page(paginator.num_pages) if paginator.num_pages > 0 else []

    # Handle form submission
    if request.method == 'POST':
        form = Todo_Form(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.save()
            messages.success(request, 'Todo Task added successfully')

    return render(request, 'todo.html', {
        'user': user,
        'user_name': user_name,
        'form': Todo_Form(),
        'todos': todos,
        'paginator': paginator,
    })