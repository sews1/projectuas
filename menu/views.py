from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'menu': '/menu',
        'home': '/',
        'foto1': 'img/product1.jpeg',
        'foto2': 'img/product2.jpeg',
        'foto3': 'img/product3.jpeg',
        'foto4': 'img/product4.png',
        'foto5': 'img/product5.png',
        'foto6': 'img/product6.png',
        'foto7': 'img/product7.png',
        'foto8': 'img/product8.png',
        'foto9': 'img/product9.png',
        'foto10': 'img/product10.png',
        'foto11': 'img/product11.png',
        'foto12': 'img/product12.png',
    }
    return render(request, 'menu.html', context)