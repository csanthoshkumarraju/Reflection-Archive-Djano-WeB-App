from django.shortcuts import render, redirect, get_object_or_404
from RA_Register_App.models import RA_RegistrationModel
from .models import MemoryModel
from django.core.paginator import Paginator
from django.contrib import messages

def memories_page(request, user_id):
    user = get_object_or_404(RA_RegistrationModel, id=user_id)
    user_name = f"{user.first_name} {user.last_name}"
    memories_list = MemoryModel.objects.filter(user=user, status="Memory")

    paginator = Paginator(memories_list, 6)
    page_number = request.GET.get('page')
    memories = paginator.get_page(page_number)

    best_list = MemoryModel.objects.filter(user=user, status='BEST')
    paginator_best = Paginator(best_list, 6)
    best_page_number = request.GET.get('best_page')
    best_memories = paginator_best.get_page(best_page_number)

    worst_list = MemoryModel.objects.filter(user=user, status='WORST')
    paginator_worst = Paginator(worst_list, 6)
    worst_page_number = request.GET.get('worst_page', '1')

    if not worst_page_number.isdigit() or int(worst_page_number) < 1:
        worst_page_number = '1'

    worst_memories = paginator_worst.get_page(int(worst_page_number))

    if request.method == 'POST':
        if 'add_memory' in request.POST:
            memory_text = request.POST.get('memory_text')
            if memory_text:
                new_memory = MemoryModel(user=user, memory=memory_text, status='Memory')
                new_memory.save()
                messages.success(request, 'Memory added successfully')
                return redirect('memories_page', user_id=user.id)

        elif 'edit_memory' in request.POST:
            memory_id = request.POST.get('memory_id')
            memory_item = get_object_or_404(MemoryModel, id=memory_id, user=user)
            request.session['editing_memory_id'] = memory_item.id
            request.session['editing_memory_text'] = memory_item.memory
            return redirect('memories_page', user_id=user.id)

        elif 'save_memory' in request.POST:
            memory_id = request.POST.get('memory_id')
            memory_text = request.POST.get('memory_text')
            if memory_id and memory_text:
                memory_item = get_object_or_404(MemoryModel, id=memory_id, user=user)
                memory_item.memory = memory_text
                memory_item.save()
                del request.session['editing_memory_id']
                del request.session['editing_memory_text']
                messages.success(request, 'Memory updated successfully')
                return redirect('memories_page', user_id=user.id)

        elif 'delete_memory' in request.POST:
            memory_id = request.POST.get('memory_id')
            memory_item = get_object_or_404(MemoryModel, id=memory_id, user=user)
            memory_item.delete()
            messages.success(request, 'Memory deleted successfully')
            return redirect('memories_page', user_id=user.id)

        elif 'mark_best' in request.POST:
            memory_id = request.POST.get('memory_id')
            if memory_id:
                memory_item = get_object_or_404(MemoryModel, id=memory_id, user=user)
                memory_item.status = 'BEST'
                memory_item.save()
                messages.success(request, 'Memory status updated to BEST')
                return redirect('memories_page', user_id=user.id)

        elif 'mark_worst' in request.POST:
            memory_id = request.POST.get('memory_id')
            if memory_id:
                memory_item = get_object_or_404(MemoryModel, id=memory_id, user=user)
                memory_item.status = 'WORST'
                memory_item.save()
                messages.success(request, 'Memory status updated to WORST')
                return redirect('memories_page', user_id=user.id)

    return render(request, 'memories.html', {
        'user': user,
        'user_name': user_name,
        'memories': memories,
        'best_memories': best_memories,
        'worst_memories': worst_memories,
        'editing_memory_id': request.session.get('editing_memory_id'),
        'editing_memory_text': request.session.get('editing_memory_text'),
    })
