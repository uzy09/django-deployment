from django.shortcuts import render

def index(request): 
    return render(request, 'index.html')

def other(request):
    return render(request, 'other.html')

def help(request): 
    return render(request, 'help.html')
