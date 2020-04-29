from django.shortcuts import render

def index(request):
    return render(request, 'homepage.html')


def codeprojects(request):
    return render(request, 'codeprojects.html')


def tattoo1891(request):
    return render(request, 'tattoo1891.html')


def aboutme(request):
    return render(request, 'aboutme.html')
