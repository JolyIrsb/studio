from django.shortcuts import render
from django.utils import timezone
from .models import Work

def main(request):
	works = Work.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'main.html', {'works': works})

def about(request):
	return render(request, 'about.html')

def designers(request):
	return render(request, 'designers.html')

def price(request):
	return render(request, 'price.html')

def contacts(request):
	return render(request, 'contacts.html')

def empty(request):
	return render(request, 'empty.html')
