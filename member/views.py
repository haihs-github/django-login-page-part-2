from django.shortcuts import render,redirect
from .models import Member

def index(request):
    id = request.session.get('user_id')  # Truy xuất user_id từ session
    member = Member.objects.all()

    context = {
        'member': member,
    }
    if id:
        context['user_id'] = id

    return render(request, 'index.html', context)

def sigin(request):
	return render(request, 'sigin.html')	

def checklogin(request):
	member = Member.objects.all()
	username = request.POST['username']
	password = request.POST['password']
	for x in member:
		if x.username == username and x.password == password:
			request.session['user_id'] = x.id
			context = {
				'member': member,
			}
			return redirect('/')
	return render(request, 'sigin.html')


