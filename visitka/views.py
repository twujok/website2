from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def about_me(request):
    return render(request, 'about_me.html')


def project(request):
    return render(request, 'project.html')

def dolboeb(request):
    return render(request, 'dolboeb.html')

def back(request):
    return render(request, 'back.html')