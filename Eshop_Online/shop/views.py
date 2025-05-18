from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
# Create your views here.

def header(request):
	context = {}
	return render(request, 'base/header.html', context)


def footer(request):
	context = {}
	return render(request, 'base/footer.html', context)


def home_page(request):
	context = {'test':'45656'}
	return render(request, 'home_page.html', context)

def contact_us_page(request):
	context = {}
	return render(request, 'contact_us.html', context)

# Authetication 

def login_page(request):

	login_form = LoginForm(request.POST or None)

	if login_form.is_valid():
		username = login_form.cleaned_data.get('username')
		password = login_form.cleaned_data.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			print('2222222222222222222')

	context = {
		'login_form' : login_form,		
	}

	return render(request, 'login.html', context)



User = get_user_model()

def register_page(request):
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        userName = register_form.cleaned_data.get('userName')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        new_user = User.objects.create_user(username=userName, email=email, password=password)
        print(new_user)

    context = {
        'title': 'Register Page',
        'message': 'Register Form',
        'register_form': register_form
    }
    return render(request, 'register_page.html', context)

