from django.shortcuts import render, redirect, get_object_or_404
from RA_Register_App.models import RA_RegistrationModel
from .models import ExperienceModel
from django.core.paginator import Paginator
from django.contrib import messages

def experiences_page(request, user_id):
    user = get_object_or_404(RA_RegistrationModel, id=user_id)
    user_name = f"{user.first_name} {user.last_name}"
    
    experiences_list = ExperienceModel.objects.filter(user=user, status="Experience")
    paginator = Paginator(experiences_list, 6)
    page_number = request.GET.get('page')
    experiences = paginator.get_page(page_number)

    good_list = ExperienceModel.objects.filter(user=user, status='GOOD')
    paginator_good = Paginator(good_list, 6)
    good_page_number = request.GET.get('good_page')
    good_experiences = paginator_good.get_page(good_page_number)

    bad_list = ExperienceModel.objects.filter(user=user, status='BAD')
    paginator_bad = Paginator(bad_list, 6)
    bad_page_number = request.GET.get('bad_page', '1')

    if not bad_page_number.isdigit() or int(bad_page_number) < 1:
        bad_page_number = '1'

    bad_experiences = paginator_bad.get_page(int(bad_page_number))

    if request.method == 'POST':
        if 'add_experience' in request.POST:
            experience_text = request.POST.get('experience_text')
            if experience_text:
                new_experience = ExperienceModel(user=user, experience=experience_text, status='Experience')
                new_experience.save()
                messages.success(request, 'Experience added successfully')
                return redirect('experiences_page', user_id=user.id)

        elif 'edit_experience' in request.POST:
            experience_id = request.POST.get('experience_id')
            experience_item = get_object_or_404(ExperienceModel, id=experience_id, user=user)
            request.session['editing_experience_id'] = experience_item.id
            request.session['editing_experience_text'] = experience_item.experience
            return redirect('experiences_page', user_id=user.id)

        elif 'save_experience' in request.POST:
            experience_id = request.POST.get('experience_id')
            experience_text = request.POST.get('experience_text')
            if experience_id and experience_text:
                experience_item = get_object_or_404(ExperienceModel, id=experience_id, user=user)
                experience_item.experience = experience_text
                experience_item.save()
                del request.session['editing_experience_id']
                del request.session['editing_experience_text']
                messages.success(request, 'Experience updated successfully')
                return redirect('experiences_page', user_id=user.id)

        elif 'delete_experience' in request.POST:
            experience_id = request.POST.get('experience_id')
            experience_item = get_object_or_404(ExperienceModel, id=experience_id, user=user)
            experience_item.delete()
            messages.success(request, 'Experience deleted successfully')
            return redirect('experiences_page', user_id=user.id)

        elif 'mark_good' in request.POST:
            experience_id = request.POST.get('experience_id')
            if experience_id:
                experience_item = get_object_or_404(ExperienceModel, id=experience_id, user=user)
                experience_item.status = 'GOOD'
                experience_item.save()
                messages.success(request, 'Experience status updated to GOOD')
                return redirect('experiences_page', user_id=user.id)

        elif 'mark_bad' in request.POST:
            experience_id = request.POST.get('experience_id')
            if experience_id:
                experience_item = get_object_or_404(ExperienceModel, id=experience_id, user=user)
                experience_item.status = 'BAD'
                experience_item.save()
                messages.success(request, 'Experience status updated to BAD')
                return redirect('experiences_page', user_id=user.id)

    return render(request, 'experiences.html', {
        'user': user,
        'user_name': user_name,
        'experiences': experiences,
        'good_experiences': good_experiences,
        'bad_experiences': bad_experiences,
        'editing_experience_id': request.session.get('editing_experience_id'),
        'editing_experience_text': request.session.get('editing_experience_text'),
    })
