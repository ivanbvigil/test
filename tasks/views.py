from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.utils import timezone

# Create your views here.

def home(request):
	tasks = Task.objects

	return render(request, 'tasks/home.html', { 'tasks' : tasks})

@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.FILES['image']:
			task = Task ()
			task.title = request.POST['title']
			task.body =  request.POST['body']
			task.image = request.FILES['image']
			task.pub_date = timezone.datetime.now()
			task.state = 'Undone'
			task.author = request.user
			task.save()
			print('url for image', task.image.url)
			return redirect('/tasks/' + str(task.id))
		else:
			return render(request, 'tasks/create.html', {'error' : 'All files are required'})	
	else:
		return render(request, 'tasks/create.html')



def detail(request, task_id):
	task = get_object_or_404(Task, pk = task_id)
	print('state init:', task.state)
	return render(request, 'tasks/detail.html', {'task' : task})

@login_required
def state_change(request, task_id):
	if request.method == 'POST':
		task = get_object_or_404(Task, pk = task_id)
		if task.state == 'Done' :
			task.state = 'Undone'
		else:
			task.state = 'Done'
		print('state:', task.state)
		task.save()
		return redirect('/tasks/' + str(task.id))

@login_required
def state_change_home(request, task_id):
	if request.method == 'POST':
		task = get_object_or_404(Task, pk = task_id)
		if task.state == 'Done' :
			task.state = 'Undone'
		else:
			task.state = 'Done'
		print('state:', task.state)
		task.save()
		return redirect('/')


	


	