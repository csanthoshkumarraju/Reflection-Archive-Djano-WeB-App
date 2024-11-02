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

    milestones = MilestoneModel.objects.filter(user=user).order_by('date_added')
    form = MilestoneForm()
    
    return render(request, 'milestones.html', {
        'user': user,
        'user_name': user_name,
        'form': form,
        'milestones': milestones,
    })
