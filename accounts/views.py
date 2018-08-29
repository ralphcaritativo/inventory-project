from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# from django.contrib.auth.decorators  import login_required


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                auth.login(request, user)
                return redirect('login')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password must match'})
    else:
        return render(request, 'accounts/signup.html')

# @login_required(login_url = "")
def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return render(request, 'dashboard.html', {'username': request.POST['username']})
		else:
			return render(request, 'accounts/login.html', {'error': 'Username or Password is incorrect! '})
	else:
		return render(request, 'accounts/login.html')

# TODO need to add to Homepage

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('login')
