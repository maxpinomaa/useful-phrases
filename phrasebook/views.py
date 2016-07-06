from django.shortcuts import render
from django.utils import timezone
from .models import Convcon

def post_list(request):
    posts = Convcon.objects.filter(audiofilulinkki='/static/Minuntiet.m4a') \
        .exclude(tagi='rus_cc')
    return render(request, 'phrasebook/post_list.html', {'posts': posts})

def reverse_list(request):
    posts = Convcon.objects.filter(tagi='fin_cq')
    return render(request, 'phrasebook/reverse_list.html', {'posts': posts})

def post_list1(request):
    posts = Convcon.objects.filter(tagi='fin_cc').order_by('-published_date')
    return render(request, 'phrasebook/fincc1.html', {'posts': posts})

def post_list2(request):
    posts = Convcon.objects.filter(tagi='fin_cc2').order_by('-published_date')
    return render(request, 'phrasebook/fincc2.html', {'posts': posts})

def post_list3(request):
    posts = Convcon.objects.filter(tagi='rus_cc').order_by('-published_date')
    return render(request, 'phrasebook/finruscc.html', {'posts': posts})

def post_list4(request):
    posts = Convcon.objects.filter(tagi='ita_cc').order_by('-published_date')
    return render(request, 'phrasebook/eng_ita_cc.html', {'posts': posts})

def post_list5(request):
    posts = Convcon.objects.filter(tagi='ita_cc2').order_by('-published_date')
    return render(request, 'phrasebook/eng_ita_cc.html', {'posts': posts})

def post_list6(request):
    posts = Convcon.objects.filter(tagi='fin_comics').order_by('-published_date')
    return render(request, 'phrasebook/fin_comics.html', {'posts': posts})

def post_list7(request):
    posts = Convcon.objects.filter(tagi='fin_fun').order_by('-published_date')
    return render(request, 'phrasebook/finfunint.html', {'posts': posts})

