from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from RA_Register_App.models import RA_RegistrationModel
from .models import GoalModel
from .forms import GoalForm
from django.contrib import messages

def goals_page(request, user_id):
    user = get_object_or_404(RA_RegistrationModel, id=user_id)
    user_name = f"{user.first_name} {user.last_name}"

    goals_list = GoalModel.objects.filter(user=user, status='Goal')
    in_progress_list = GoalModel.objects.filter(user=user, status='In Progress')
    completed_list = GoalModel.objects.filter(user=user, status='Completed')

    paginator_goals = Paginator(goals_list, 6)
    page_number = request.GET.get('page')
    goals_page = paginator_goals.get_page(page_number)

    paginator_in_progress = Paginator(in_progress_list, 6)
    in_progress_page_number = request.GET.get('in_progress_page')
    in_progress_page = paginator_in_progress.get_page(in_progress_page_number)

    paginator_completed = Paginator(completed_list, 6)
    completed_page_number = request.GET.get('completed_page')
    completed_page = paginator_completed.get_page(completed_page_number)

    if request.method == 'POST':
        if 'add_goal' in request.POST:
            goal_text = request.POST.get('goal_text')
            if goal_text:
                new_goal = GoalModel(user=user, goal=goal_text, status='Goal')
                new_goal.save()
                messages.success(request, 'Goal added successfully')
                return redirect('goals_page', user_id=user.id)

        elif 'edit_goal' in request.POST:
            goal_id = request.POST.get('goal_id')
            goal_item = get_object_or_404(GoalModel, id=goal_id, user=user)
            request.session['editing_goal_id'] = goal_item.id
            request.session['editing_goal_text'] = goal_item.goal
            return redirect('goals_page', user_id=user.id)

        elif 'save_goal' in request.POST:
            goal_id = request.POST.get('goal_id')
            goal_text = request.POST.get('goal_text')
            if goal_id and goal_text:
                goal_item = get_object_or_404(GoalModel, id=goal_id, user=user)
                goal_item.goal = goal_text
                goal_item.save()
                del request.session['editing_goal_id']
                del request.session['editing_goal_text']
                messages.success(request, 'Goal updated successfully')
                return redirect('goals_page', user_id=user.id)

        elif 'mark_in_progress' in request.POST:
            goal_id = request.POST.get('goal_id')
            if goal_id:
                goal_item = get_object_or_404(GoalModel, id=goal_id, user=user)
                goal_item.status = 'In Progress'
                goal_item.save()
                messages.success(request, 'Goal status updated to In Progress')
                return redirect('goals_page', user_id=user.id)

        elif 'complete_task' in request.POST:
            goal_id = request.POST.get('goal_id')
            if goal_id:
                goal_item = get_object_or_404(GoalModel, id=goal_id, user=user)
                goal_item.status = 'Completed'
                goal_item.save()
                messages.success(request, 'Goal marked as completed')
                return redirect('goals_page', user_id=user.id)

        elif 'delete_goal' in request.POST:
            goal_id = request.POST.get('goal_id')
            if goal_id:
                goal_item = get_object_or_404(GoalModel, id=goal_id, user=user)
                goal_item.delete()
                messages.success(request, 'Goal deleted successfully')
                return redirect('goals_page', user_id=user.id)

    return render(request, 'goals.html', {
        'user': user,
        'user_name': user_name,
        'form': GoalForm(),
        'goals': goals_page,
        'in_progress_tasks': in_progress_page,
        'completed_tasks': completed_page,
        'editing_goal_id': request.session.get('editing_goal_id'),
        'editing_goal_text': request.session.get('editing_goal_text'),
    })


