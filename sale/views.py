from django.shortcuts import render
from .models import Plus,PSN,Game
from django.db.models import Q

# Create your views here.


def homepage_view(request):
    return render(request, 'home.html')


def plus_view(request):
    plus = Plus.objects.all()
    return render(request, 'sale/plus.html', {'plus': plus})


def detail_view(request, id):
    plus = Plus.objects.get(id=id)
    return render(request, "sale/detailplus.html", {'plus': plus})

def psn_detail_view(request, id):
    plus = PSN.objects.get(id=id)
    return render(request, "sale/detailpsn.html", {'psn': plus})

def psn_view(request):
    psn = PSN.objects.all()
    return render(request,"sale/psn.html",{'psn':psn})


def rent_view(request):
    return render(request, 'icare.html')

def game_view(request):
    game = Game.objects.all()
    query = request.GET.get('q')
    if query:
        game = game.filter(
            Q(name__icontains=query)
        ).distinct()
    return render(request,'sale/game.html',{'plus':game})

def game_detail(request,id):
    game = Game.objects.get(id=id)
    return render(request,'sale/gamedetail.html',{'psn':game})
