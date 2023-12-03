from django.shortcuts import render, redirect

from .models import *
# Create your views here.


def cal_timers():
    timer = timers.objects.all()
    if len(timer) == 1:
        timer = timers.objects.get(name="DEF")
    else:
        timer = timers.objects.get(name="USER Timer")
    return timer


def index(request):
    timer = cal_timers
    Tasks = tasks.objects.all()
    return render(request, 'index.html', {"timer": timer, "tasks": Tasks})


def settings(request):
    if request.method == "POST":
        pomodoro = request.POST["PomodoroMinutes"]
        short_break = request.POST["short_breakMinutes"]
        long_break = request.POST["long_breakMinutes"]
        new_timer = timers.objects.create(
            pomodoro=pomodoro, short_break=short_break, long_break=long_break, name="USER Timer")
        new_timer.save()
        timer = cal_timers
        response = redirect('settings')
        return response
    else:
        timer = cal_timers
        return render(request, 'settings.html', {"timer": timer})


def delete_timer(request):
    user_timer = timers.objects.filter(name="USER Timer")
    if user_timer != None:
        user_timer.delete()
    return redirect('settings')


def add_task(request):
    if request.method == "POST":
        task_desc = request.POST["task_desc"]
        est_pomodoro = request.POST["est_pomodoro"]
        new_task = tasks.objects.create(
            task_desc=task_desc, est_pomodoro=est_pomodoro)
        new_task.save()

        return redirect("index")
    else:
        return render(request, "add_task.html")


def delete_task(request, task_id):
    task = tasks.objects.get(custom_id=task_id)
    task.delete()
    return redirect('index')
