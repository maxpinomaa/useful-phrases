from django.shortcuts import render
from django.utils import timezone
from .models import Convcon

def post_list(request):
    posts = Convcon.objects.filter(audiofilulinkki='/static/Minuntiet.m4a') \
        .exclude(tagi='rus_cc')
    return render(request, 'phrasebook/post_list.html', {'posts': posts})

def reverse_list(request):
    posts = Convcon.objects.filter(tagi='fin_cq').order_by('-published_date')
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
    return render(request, 'phrasebook/eng_ita_cc2.html', {'posts': posts})

def post_list6(request):
    posts = Convcon.objects.filter(tagi='fin_comics').order_by('-published_date')
    return render(request, 'phrasebook/fin_comics.html', {'posts': posts})

def post_list7(request):
    posts = Convcon.objects.filter(tagi='fin_fun').order_by('-published_date')
    return render(request, 'phrasebook/finfunint.html', {'posts': posts})

def post_list8(request):
    posts = Convcon.objects.filter(audiofilulinkki='/static/Minuntiet.m4a') \
        .exclude(tagi='fin_cc')
    return render(request, 'phrasebook/post_list_rus.html', {'posts': posts})

def post_list9(request):
    posts = Convcon.objects.filter(tagi='rus_fun').order_by('-published_date')
    return render(request, 'phrasebook/rusfinfun.html', {'posts': posts})

def post_list10(request):
    posts = Convcon.objects.filter(connector='quando ero bambino').order_by('-published_date')
    return render(request, 'phrasebook/post_list_ita.html', {'posts': posts})

def post_list11(request):
    posts = Convcon.objects.filter(connector='hasta donde yo sé').order_by('-published_date')
    return render(request, 'phrasebook/front_spa.html', {'posts': posts})

def post_list12(request):
    posts = Convcon.objects.filter(tagi='spa_fun').order_by('-published_date')
    return render(request, 'phrasebook/espfun.html', {'posts': posts})

def post_list13(request):
    posts = Convcon.objects.filter(tagi='rus_cq').order_by('-published_date')
    return render(request, 'phrasebook/reverse_list_rus.html', {'posts': posts})

def post_list14(request):
    posts = Convcon.objects.filter(tagi='rus_cc2').order_by('-published_date')
    return render(request, 'phrasebook/finruscc2.html', {'posts': posts})

def post_list15(request):
    posts = Convcon.objects.filter(tagi='spa_cc1').order_by('-published_date')
    return render(request, 'phrasebook/esp_cc1.html', {'posts': posts})

def post_list16(request):
    posts = Convcon.objects.filter(tagi='ita_cq').order_by('-published_date')
    return render(request, 'phrasebook/common_questions_it.html', {'posts': posts})

def post_list17(request):
    posts = Convcon.objects.filter(tagi='fun_ita').order_by('-published_date')
    return render(request, 'phrasebook/ita_fun.html', {'posts': posts})






