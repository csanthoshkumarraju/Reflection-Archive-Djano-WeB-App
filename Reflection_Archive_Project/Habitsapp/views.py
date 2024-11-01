from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from RA_Register_App.models import RA_RegistrationModel
from django.contrib import messages
from .models import HabitModel

def habits_page(request, user_id):
    user = get_object_or_404(RA_RegistrationModel, id=user_id)
    user_name = f"{user.first_name} {user.last_name}"

    # Fetching habits for "To Do"
    habits_list = HabitModel.objects.filter(user=user, status='To Do')
    paginator_habits = Paginator(habits_list, 6)
    page_number = request.GET.get('page')
    habits_page = paginator_habits.get_page(page_number)

    # Fetching habits for "In Progress"
    in_progress_list = HabitModel.objects.filter(user=user, status='In Progress')
    paginator_in_progress = Paginator(in_progress_list, 6)
    page_number_in_progress = request.GET.get('page_in_progress')
    in_progress_habits = paginator_in_progress.get_page(page_number_in_progress)

    # Fetching habits for "Completed"
    completed_list = HabitModel.objects.filter(user=user, status='Completed')
    paginator_completed = Paginator(completed_list, 6)
    completed_page_number = request.GET.get('completed_page')
    completed_habits = paginator_completed.get_page(completed_page_number)

    if request.method == 'POST':
        if 'add_habit' in request.POST:
            habit_text = request.POST.get('habit_text')
            if habit_text:
                new_habit = HabitModel(user=user, habit=habit_text, status='To Do')
                new_habit.save()
                messages.success(request, 'Habit added successfully')
                return redirect('habits_page', user_id=user.id)

        elif 'edit_habit' in request.POST:
            habit_id = request.POST.get('habit_id')
            habit_item = get_object_or_404(HabitModel, id=habit_id, user=user)
            request.session['editing_habit_id'] = habit_item.id
            request.session['editing_habit_text'] = habit_item.habit
            return redirect('habits_page', user_id=user.id)

        elif 'save_habit' in request.POST:
            habit_id = request.POST.get('habit_id')
            habit_text = request.POST.get('habit_text')
            if habit_id and habit_text:
                habit_item = get_object_or_404(HabitModel, id=habit_id, user=user)
                habit_item.habit = habit_text
                habit_item.save()
                del request.session['editing_habit_id']
                del request.session['editing_habit_text']
                messages.success(request, 'Habit updated successfully')
                return redirect('habits_page', user_id=user.id)

        elif 'mark_in_progress' in request.POST:
            habit_id = request.POST.get('habit_id')
            habit_item = get_object_or_404(HabitModel, id=habit_id, user=user)
            habit_item.status = 'In Progress'
            habit_item.save()
            messages.success(request, 'Habit marked as in progress')
            return redirect('habits_page', user_id=user.id)

        elif 'mark_complete' in request.POST:
            habit_id = request.POST.get('habit_id')
            habit_item = get_object_or_404(HabitModel, id=habit_id, user=user)
            habit_item.status = 'Completed'
            habit_item.save()
            messages.success(request, 'Habit marked as complete')
            return redirect('habits_page', user_id=user.id)

        elif 'delete_habit' in request.POST:
            habit_id = request.POST.get('habit_id')
            habit_item = get_object_or_404(HabitModel, id=habit_id, user=user)
            habit_item.delete()
            messages.success(request, 'Habit deleted successfully')
            return redirect('habits_page', user_id=user.id)

    return render(request, 'habits.html', {
        'user': user,
        'user_name': user_name,
        'habits': habits_page,
        'in_progress_habits': in_progress_habits,
        'completed_habits': completed_habits,  # Add this line
        'editing_habit_id': request.session.get('editing_habit_id'),
        'editing_habit_text': request.session.get('editing_habit_text'),
    })
