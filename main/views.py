from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Todo
from django.urls import reverse


def home(request):
    return render(request, 'base.html')


def add(request):
    todo_items = Todo.objects.all().order_by('added_date')
    return render(request, 'main/index.html', {"todo_items": todo_items})


@csrf_exempt
def add_items(request):
    # print(request.POST)
    date = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(added_date=date, text=content)
    return HttpResponseRedirect(reverse('main:add'))


@csrf_exempt
def delete_items(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse('main:add'))
