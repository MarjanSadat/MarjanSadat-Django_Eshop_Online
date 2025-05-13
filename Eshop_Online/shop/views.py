from django.shortcuts import render

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