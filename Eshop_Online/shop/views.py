from django.shortcuts import render

# Create your views here.

def home_page(request):
	context = {'test':'45656'}
	return render(request, 'home_page.html', context)