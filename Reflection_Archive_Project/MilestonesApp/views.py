from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from RA_Register_App.models import RA_RegistrationModel
from .models import MilestoneModel
from .forms import MilestoneForm
from django.contrib import messages

def milestones_page(request, user_id):
    user = get_object_or_404(RA_RegistrationModel, id=user_id)
    user_name = f"{user.first_name} {user.last_name}"

    if request.method == 'POST':
        if 'add_milestone' in request.POST:
            form = MilestoneForm(request.POST)
            if form.is_valid():
                new_milestone = form.save(commit=False)
                new_milestone.user = user
                new_milestone.date_added = timezone.now().date()
                new_milestone.save()
                messages.success(request, 'Milestone added successfully')
                return redirect('milestones_page', user_id=user.id)

        elif 'delete_milestone' in request.POST:
            milestone_id = request.POST.get('milestone_id')
            if milestone_id:
                milestone_item = get_object_or_404(MilestoneModel, id=milestone_id, user=user)
                milestone_item.delete()
                messages.success(request, 'Milestone deleted successfully')
                return redirect('milestones_page', user_id=user.id)

        elif 'edit_milestone' in request.POST:
            milestone_id = request.POST.get('milestone_id')
            milestone_item = get_object_or_404(MilestoneModel, id=milestone_id, user=user)
            request.session['editing_milestone_id'] = milestone_item.id
            request.session['editing_milestone_text'] = milestone_item.milestone
            return redirect('milestones_page', user_id=user.id)

        elif 'save_milestone' in request.POST:
            milestone_id = request.POST.get('milestone_id')
            milestone_text = request.POST.get('milestone_text')
            if milestone_id and milestone_text:
                milestone_item = get_object_or_404(MilestoneModel, id=milestone_id, user=user)
                milestone_item.milestone = milestone_text
                milestone_item.save()
                del request.session['editing_milestone_id']
                del request.session['editing_milestone_text']
                messages.success(request, 'Milestone updated successfully')
                return redirect('milestones_page', user_id=user.id)

    milestones = MilestoneModel.objects.filter(user=user).order_by('date_added')

    return render(request, 'milestones.html', {
        'milestones': milestones,
        'editing_milestone_id': request.session.get('editing_milestone_id'),
        'editing_milestone_text': request.session.get('editing_milestone_text'),
        'user_name':user_name,
    })
