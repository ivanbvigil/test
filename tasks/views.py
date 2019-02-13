from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.utils import timezone

# Create your views here.

def home(request):

	return render(request, 'tasks/home.html')

@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.FILES['image']:
			task = Task ()
			task.title = request.POST['title']
			task.body =  request.POST['body']

			#if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
			#	task.url = request.POST['url']
			#else:
			#	task.url = 'http://' + request.POST['url']	
			
			task.image = request.FILES['image']
			task.pub_date = timezone.datetime.now()
			task.votes_total = 1
			task.author = request.user
			task.save()
			return redirect('home')
		else:
			return render(request, 'tasks/create.html', {'error' : 'All files are required'})	
	else:
		return render(request, 'tasks/create.html')