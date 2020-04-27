from django.shortcuts import render

def index(request):
    return render(request, 'homepage.html')


def projects(request):
    return render(request, 'codeprojects.html')


def rivers(request):
    return render(request, 'tattoo1897.html')


def aboutme(request):
    return render(request, 'aboutme.html')
