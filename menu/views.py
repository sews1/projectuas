from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'menu': '/menu',
        'home': '/',
    }
    return render(request, 'menu.html', context)