from django.shortcuts import render
from RA_Register_App.models import RA_RegistrationModel
from ToDoApp.models import todo_model  
from PlansApp.models import plan_model
from AchievementApp.models import acheivements_model
from TravellingApp.models import TravelModel
from ExeperienceApp.models import ExperienceModel
from Habitsapp.models import HabitModel
from MemoriesApp.models import MemoryModel
from LifegoalsApp.models import GoalModel
from MilestonesApp.models import MilestoneModel

def dashboard(request, user_id):
    user = RA_RegistrationModel.objects.get(id=user_id)
    user_name = f"{user.first_name} {user.last_name}"
    
    todo_count = todo_model.objects.filter(user=user, status='To Do').count()
    in_progress_count = todo_model.objects.filter(user=user, status='In Progress').count()
    completed_count = todo_model.objects.filter(user=user, status='Completed').count()

    plan_count = plan_model.objects.filter(user=user, status='Plan').count()
    plan_in_progress_count = plan_model.objects.filter(user=user, status='In Progress').count()
    plan_completed_count = plan_model.objects.filter(user=user, status='Completed').count()

    Achievements_count = acheivements_model.objects.filter(user=user, achievment_status='achievement').count()
    Achievements_in_progress_count = acheivements_model.objects.filter(user=user, achievment_status='In Progress').count()
    Achievements_completed_count = acheivements_model.objects.filter(user=user, achievment_status='Completed').count()

    Travelling_count = TravelModel.objects.filter(user=user, status='To Do').count()
    Travelling_in_progress_count = TravelModel.objects.filter(user=user, status='In Progress').count()
    Travelling_completed_count = TravelModel.objects.filter(user=user, status='Completed').count()

    Experiences_count = ExperienceModel.objects.filter(user=user, status="Experience").count()
    Experiences_in_progress_count = ExperienceModel.objects.filter(user=user, status='GOOD').count()
    Experiences_completed_count  = ExperienceModel.objects.filter(user=user, status='BAD').count()

    Habits_count = HabitModel.objects.filter(user=user, status='To Do').count()
    Habits_in_progress_count = HabitModel.objects.filter(user=user, status='In Progress').count()
    Habits_completed_count = HabitModel.objects.filter(user=user, status='Completed').count()

    Memories_in_progress_count = MemoryModel.objects.filter(user=user, status='BEST').count()
    Memories_completed_count = MemoryModel.objects.filter(user=user, status='WORST').count()

    Goals_count = GoalModel.objects.filter(user=user, status='Goal').count()
    Goals_in_progress_count = GoalModel.objects.filter(user=user, status='In Progress').count()
    Goals_completed_count = GoalModel.objects.filter(user=user, status='Completed').count()

    milestone_count = MilestoneModel.objects.filter(user=user).count()


    return render(request, 'dashboard.html', {
        'user': user,
        'user_name': user_name,
        'todo_count': todo_count,
        'in_progress_count': in_progress_count,
        'completed_count': completed_count,
        'plan_count':plan_count,
        'plan_in_progress_count':plan_in_progress_count,
        'plan_completed_count':plan_completed_count,
        'Achievements_count':Achievements_count,
        'Achievements_in_progress_count':Achievements_in_progress_count,
        'Achievements_completed_count':Achievements_completed_count,
        'Travelling_count':Travelling_count,
        'Travelling_in_progress_count':Travelling_in_progress_count,
        'Travelling_completed_count':Travelling_completed_count,
        'Experiences_count':Experiences_count,
        'Experiences_in_progress_count':Experiences_in_progress_count,
        'Experiences_completed_count':Experiences_completed_count,
        'Habits_count':Habits_count,
        'Habits_in_progress_count':Habits_in_progress_count,
        'Habits_completed_count':Habits_completed_count,
        'Memories_in_progress_count':Memories_in_progress_count,
        'Memories_completed_count':Memories_completed_count,
        'Goals_count':Goals_count,
        'Goals_in_progress_count':Goals_in_progress_count,
        'Goals_completed_count':Goals_completed_count,
        'milestone_count':milestone_count,
    })
