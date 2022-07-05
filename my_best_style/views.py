from django.shortcuts import render

def welcome(request):
    context = {
        'menu' : '/menu',
        'home' : '/',
    }
    return render(request, 'index.html', context)