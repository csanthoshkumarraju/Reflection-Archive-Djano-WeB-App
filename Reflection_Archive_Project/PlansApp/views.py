# from django.shortcuts import render,get_object_or_404
# from RA_Register_App.models import RA_RegistrationModel
# # Create your views here.

# def plans_page(request,user_id):
#     user = get_object_or_404(RA_RegistrationModel, id=user_id)
#     user_name = f"{user.first_name} {user.last_name}"

#     return render(request, 'plans.html', {
#         'user': user,
#         'user_name': user_name,
#     })

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from RA_Register_App.models import RA_RegistrationModel
from .models import plan_model
from .forms import Plan_Form
from django.contrib import messages

def plans_page(request, user_id):
    user = get_object_or_404(RA_RegistrationModel, id=user_id)
    user_name = f"{user.first_name} {user.last_name}"

    plans_list = plan_model.objects.filter(user=user, status='Plan')
    in_progress_list = plan_model.objects.filter(user=user, status='In Progress')
    completed_list = plan_model.objects.filter(user=user, status='Completed')

    paginator_plans = Paginator(plans_list, 6)
    page_number = request.GET.get('page')
    plans_page = paginator_plans.get_page(page_number)

    paginator_in_progress = Paginator(in_progress_list, 6)
    in_progress_page_number = request.GET.get('in_progress_page')
    in_progress_page = paginator_in_progress.get_page(in_progress_page_number)

    paginator_completed = Paginator(completed_list, 6)
    completed_page_number = request.GET.get('completed_page')
    completed_page = paginator_completed.get_page(completed_page_number)

    if request.method == 'POST':
        if 'add_plan' in request.POST:
            plan_text = request.POST.get('plan_text')
            if plan_text:
                new_plan = plan_model(user=user, plan=plan_text, status='Plan')
                new_plan.save()
                messages.success(request, 'Plan added successfully')
                return redirect('plans_page', user_id=user.id)

        elif 'edit_plan' in request.POST:
            plan_id = request.POST.get('plan_id')
            plan_item = get_object_or_404(plan_model, id=plan_id, user=user)
            request.session['editing_plan_id'] = plan_item.id
            request.session['editing_plan_text'] = plan_item.plan
            return redirect('plans_page', user_id=user.id)

        elif 'save_plan' in request.POST:
            plan_id = request.POST.get('plan_id')
            plan_text = request.POST.get('plan_text')
            if plan_id and plan_text:
                plan_item = get_object_or_404(plan_model, id=plan_id, user=user)
                plan_item.plan = plan_text
                plan_item.save()
                del request.session['editing_plan_id']
                del request.session['editing_plan_text']
                messages.success(request, 'Plan updated successfully')
                return redirect('plans_page', user_id=user.id)

        elif 'mark_in_progress' in request.POST:
            plan_id = request.POST.get('plan_id')
            if plan_id:
                plan_item = get_object_or_404(plan_model, id=plan_id, user=user)
                plan_item.status = 'In Progress'
                plan_item.save()
                messages.success(request, 'Plan status updated to In Progress')
                return redirect('plans_page', user_id=user.id)

        elif 'complete_task' in request.POST:
            plan_id = request.POST.get('plan_id')
            if plan_id:
                plan_item = get_object_or_404(plan_model, id=plan_id, user=user)
                plan_item.status = 'Completed'
                plan_item.save()
                messages.success(request, 'Plan marked as completed')
                return redirect('plans_page', user_id=user.id)

        elif 'delete_plan' in request.POST:
            plan_id = request.POST.get('plan_id')
            if plan_id:
                plan_item = get_object_or_404(plan_model, id=plan_id, user=user)
                plan_item.delete()
                messages.success(request, 'Plan deleted successfully')
                return redirect('plans_page', user_id=user.id)

    return render(request, 'plans.html', {
        'user': user,
        'user_name': user_name,
        'form': Plan_Form(),
        'plans': plans_page,
        'in_progress_tasks': in_progress_page,
        'completed_tasks': completed_page,
        'editing_plan_id': request.session.get('editing_plan_id'),
        'editing_plan_text': request.session.get('editing_plan_text'),
    })
