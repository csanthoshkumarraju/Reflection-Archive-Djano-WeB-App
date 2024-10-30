from django.shortcuts import render, redirect, get_object_or_404
from RA_Register_App.models import RA_RegistrationModel
from .models import acheivements_model
from .forms import AchievementsForm
from django.core.paginator import Paginator
from django.contrib import messages

def achievements_page(request, user_id):
    user = get_object_or_404(RA_RegistrationModel, id=user_id)
    user_name = f"{user.first_name} {user.last_name}"

    achievements_list = acheivements_model.objects.filter(user=user, achievment_status='achievement')
    in_progress_list = acheivements_model.objects.filter(user=user, achievment_status='In Progress')
    completed_list = acheivements_model.objects.filter(user=user, achievment_status='Completed')

    paginator_achievements = Paginator(achievements_list, 6)
    page_number = request.GET.get('page')
    achievements_page = paginator_achievements.get_page(page_number)

    paginator_in_progress = Paginator(in_progress_list, 6)
    in_progress_page_number = request.GET.get('in_progress_page')
    in_progress_page = paginator_in_progress.get_page(in_progress_page_number)

    paginator_completed = Paginator(completed_list, 6)
    completed_page_number = request.GET.get('completed_page')
    completed_page = paginator_completed.get_page(completed_page_number)

    if request.method == 'POST':
        if 'add_achievement' in request.POST:
            achievement_text = request.POST.get('achievement_text')
            if achievement_text:
                new_achievement = acheivements_model(user=user, acheiement=achievement_text, achievment_status='achievement')
                new_achievement.save()
                messages.success(request, 'Achievement added successfully')
                return redirect('achievements_page', user_id=user.id)

        elif 'edit_achievement' in request.POST:
            achievement_id = request.POST.get('achievement_id')
            achievement_item = get_object_or_404(acheivements_model, id=achievement_id, user=user)
            request.session['editing_achievement_id'] = achievement_item.id
            request.session['editing_achievement_text'] = achievement_item.acheiement
            return redirect('achievements_page', user_id=user.id)

        elif 'save_achievement' in request.POST:
            achievement_id = request.POST.get('achievement_id')
            achievement_text = request.POST.get('achievement_text')
            if achievement_id and achievement_text:
                achievement_item = get_object_or_404(acheivements_model, id=achievement_id, user=user)
                achievement_item.acheiement = achievement_text
                achievement_item.save()
                del request.session['editing_achievement_id']
                del request.session['editing_achievement_text']
                messages.success(request, 'Achievement updated successfully')
                return redirect('achievements_page', user_id=user.id)

        elif 'mark_in_progress' in request.POST:
            achievement_id = request.POST.get('achievement_id')
            if achievement_id:
                achievement_item = get_object_or_404(acheivements_model, id=achievement_id, user=user)
                achievement_item.achievment_status = 'In Progress'
                achievement_item.save()
                messages.success(request, 'Achievement status updated to In Progress')
                return redirect('achievements_page', user_id=user.id)

        elif 'complete_task' in request.POST:
            achievement_id = request.POST.get('achievement_id')
            if achievement_id:
                achievement_item = get_object_or_404(acheivements_model, id=achievement_id, user=user)
                achievement_item.achievment_status = 'Completed'
                achievement_item.save()
                messages.success(request, 'Achievement marked as completed')
                return redirect('achievements_page', user_id=user.id)

        elif 'delete_achievement' in request.POST:
            achievement_id = request.POST.get('achievement_id')
            if achievement_id:
                achievement_item = get_object_or_404(acheivements_model, id=achievement_id, user=user)
                achievement_item.delete()
                messages.success(request, 'Achievement deleted successfully')
                return redirect('achievements_page', user_id=user.id)

    return render(request, 'acheivements.html', {
        'user': user,
        'user_name': user_name,
        'form': AchievementsForm(),
        'achievements': achievements_page,
        'in_progress_tasks': in_progress_page,
        'completed_tasks': completed_page,
        'editing_achievement_id': request.session.get('editing_achievement_id'),
        'editing_achievement_text': request.session.get('editing_achievement_text'),
    })
