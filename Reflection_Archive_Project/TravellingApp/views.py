from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from RA_Register_App.models import RA_RegistrationModel
from .models import TravelModel
from .forms import TravelForm
from django.contrib import messages

def travel_page(request, user_id):
    user = get_object_or_404(RA_RegistrationModel, id=user_id)
    user_name = f"{user.first_name} {user.last_name}"

    travels_list = TravelModel.objects.filter(user=user, status='To Do')
    in_progress_travels = TravelModel.objects.filter(user=user, status='In Progress')
    completed_travels = TravelModel.objects.filter(user=user, status='Completed')  # Added for completed

    paginator_travels = Paginator(travels_list, 6)
    page_number = request.GET.get('page')
    travels_page = paginator_travels.get_page(page_number)

    paginator_in_progress = Paginator(in_progress_travels, 6)
    in_progress_page_number = request.GET.get('in_progress_page')
    in_progress_travels = paginator_in_progress.get_page(in_progress_page_number)

    paginator_completed = Paginator(completed_travels, 6)  # Added for pagination of completed
    completed_page_number = request.GET.get('completed_page')
    completed_travels_page = paginator_completed.get_page(completed_page_number)

    if request.method == 'POST':
        if 'add_travel' in request.POST:
            travel_text = request.POST.get('destination')
            if travel_text:
                new_travel = TravelModel(user=user, destination=travel_text, status='To Do')
                new_travel.save()
                messages.success(request, 'Travel destination added successfully')
                return redirect('travel_page', user_id=user.id)

        elif 'edit_travel' in request.POST:
            travel_id = request.POST.get('travel_id')
            travel_item = get_object_or_404(TravelModel, id=travel_id, user=user)
            request.session['editing_travel_id'] = travel_item.id
            request.session['editing_travel_text'] = travel_item.destination
            return redirect('travel_page', user_id=user.id)

        elif 'save_travel' in request.POST:
            travel_id = request.POST.get('travel_id')
            travel_text = request.POST.get('destination')
            if travel_id and travel_text:
                travel_item = get_object_or_404(TravelModel, id=travel_id, user=user)
                travel_item.destination = travel_text
                travel_item.save()
                del request.session['editing_travel_id']
                del request.session['editing_travel_text']
                messages.success(request, 'Travel destination updated successfully')
                return redirect('travel_page', user_id=user.id)

        elif 'mark_in_progress' in request.POST:
            travel_id = request.POST.get('travel_id')
            if travel_id:
                travel_item = get_object_or_404(TravelModel, id=travel_id, user=user)
                travel_item.status = 'In Progress'
                travel_item.save()
                messages.success(request, 'Travel status updated to In Progress')
                return redirect('travel_page', user_id=user.id)

        elif 'complete_task' in request.POST:  # Completed section
            travel_id = request.POST.get('travel_id')
            if travel_id:
                travel_item = get_object_or_404(TravelModel, id=travel_id, user=user)
                travel_item.status = 'Completed'
                travel_item.save()
                messages.success(request, 'Travel marked as completed')
                return redirect('travel_page', user_id=user.id)

        elif 'delete_travel' in request.POST:
            travel_id = request.POST.get('travel_id')
            if travel_id:
                travel_item = get_object_or_404(TravelModel, id=travel_id, user=user)
                travel_item.delete()
                messages.success(request, 'Travel destination deleted successfully')
                return redirect('travel_page', user_id=user.id)

    return render(request, 'travelling.html', {
        'user_name': user_name,
        'travels': travels_page,
        'in_progress_travels': in_progress_travels,
        'completed_travels': completed_travels_page,  # Added for completed travels
        'editing_travel_id': request.session.get('editing_travel_id'),
        'editing_travel_text': request.session.get('editing_travel_text'),
    })
