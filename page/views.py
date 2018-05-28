from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1><center>Привет мир!</center></h1> \
    	                 <a href='second/'>Вторая страница </a> \
    	                 <a href='third/'>Третья страница </a>")
def second(request):
    return render(request, "page/second.html")

def third(request):
	return render(request, 'page/third.html')
	