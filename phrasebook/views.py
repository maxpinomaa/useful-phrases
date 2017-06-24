from django.shortcuts import render
from django.utils import timezone
from .models import Convcon
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    posts = Convcon.objects.filter(audiofilulinkki='/static/Minuntiet.m4a') \
        .exclude(tagi='rus_cc')
    return render(request, 'phrasebook/post_list.html', {'posts': posts})

def reverse_list(request):
    posts = Convcon.objects.filter(tagi='fin_cq').order_by('-published_date')
    return render(request, 'phrasebook/reverse_list.html', {'posts': posts})

def post_list1(request):
    posts = Convcon.objects.filter(tagi='fin_cc').order_by('-published_date') \
        .exclude(exampletransl='---')
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
    posts = Convcon.objects.all()
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'phrasebook/rusfinfun.html', {'posts': posts})

def post_list10(request):
    posts = Convcon.objects.filter(connector='Quando ero bambino').order_by('-published_date')
    return render(request, 'phrasebook/post_list_ita.html', {'posts': posts})

def post_list11(request):
    posts = Convcon.objects.filter(connector='Me pregunto').order_by('-published_date')
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

def post_list18(request):
    posts = Convcon.objects.filter(tagi='spa_cq').order_by('-published_date')
    return render(request, 'phrasebook/common_questions_spa.html', {'posts': posts})

def post_list19(request):
    posts = Convcon.objects.filter(tagi='spa_cqfaf').order_by('-published_date')
    return render(request, 'phrasebook/languages.html', {'posts': posts})

def post_list20(request):
    posts = Convcon.objects.filter(tagi='spa_cqfaf').order_by('-published_date')
    return render(request, 'phrasebook/dialogue_fin.html', {'posts': posts})

def post_list21(request):
    posts = Convcon.objects.filter(connector='когда я был ребенком').order_by('-published_date')
    return render(request, 'phrasebook/front_rus.html', {'posts': posts})

def post_list22(request):
    posts = Convcon.objects.filter(tagi='rus_eng_cc').order_by('-published_date')
    return render(request, 'phrasebook/rus_conversational.html', {'posts': posts})

def post_list23(request):
    posts = Convcon.objects.filter(tagi='rus_eng_fun').order_by('-published_date')
    return render(request, 'phrasebook/rus_fun.html', {'posts': posts})

def post_list24(request):
    posts = Convcon.objects.filter(tagi='rus_eng_cq').order_by('-published_date')
    return render(request, 'phrasebook/common_questions_rus.html', {'posts': posts})

def post_list25(request):
    posts = Convcon.objects.filter(tagi='feafeafae').order_by('-published_date')
    return render(request, 'phrasebook/learning_tips.html', {'posts': posts})

def post_list26(request):
    posts = Convcon.objects.filter(tagi='feafe6afae').order_by('-published_date')
    return render(request, 'phrasebook/fin_cq_quiz.html', {'posts': posts})

def post_list27(request):
    posts = Convcon.objects.filter(tagi='feafe6afae').order_by('-published_date')
    return render(request, 'phrasebook/fin_cc_quiz.html', {'posts': posts})

def post_list28(request):
    posts = Convcon.objects.filter(tagi='feafe6afae').order_by('-published_date')
    return render(request, 'phrasebook/esp_cq_quiz.html', {'posts': posts})

def post_list29(request):
    posts = Convcon.objects.filter(tagi='feafe6afae').order_by('-published_date')
    return render(request, 'phrasebook/esp_cc_quiz.html', {'posts': posts})

def post_list30(request):
    posts = Convcon.objects.filter(tagi='ita_cc2').order_by('-published_date')
    return render(request, 'phrasebook/eng_ita_cc2.html', {'posts': posts})

def post_list31(request):
    posts = Convcon.objects.filter(tagi='spa_cc2').order_by('-published_date')
    return render(request, 'phrasebook/esp_cc2.html', {'posts': posts})


