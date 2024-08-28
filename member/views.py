from django.shortcuts import render,redirect
from .models import Member
from django.contrib.sessions.models import Session
from django.contrib import messages

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
			messages.success(request, "Bạn đã đăng nhập thành công!")
			return redirect('/')
	return render(request, 'sigin.html')

def sigout(request):
	request.session.flush()
	return redirect('/')

def sigup(request):
	return render(request, 'sigup.html')

def checksigup(request):
	username = request.POST['username']
	password = request.POST['password']
	repassword = request.POST['repassword']
	phonenumber = request.POST['phonenumber']
	realname = request.POST['realname']
	membernames = list(Member.objects.values_list('username', flat=True))
	print('ten nguoi dung',membernames)
	if username in membernames:
		return redirect('/')
	elif password == repassword:
		member = Member(username=username, password=password, phonenumber=phonenumber, realname=realname)
		member.save()
		return redirect('/')
	return redirect('/')

def delete(request, id):
	member = Member.objects.get(id=id)
	member.delete()
	return redirect('/')
    
def getedit(request, id):
	member = Member.objects.get(id=id)
	return render(request, 'edit.html', {'member': member})

def update(request, id):
	member = Member.objects.get(id=id)
	member.username = request.POST['username']
	member.password = request.POST['password']
	member.phonenumber = request.POST['phonenumber']
	member.realname = request.POST['realname']
	member.save()
	return redirect('/')
	
