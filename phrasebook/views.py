from django.shortcuts import render
from django.utils import timezone
from .models import Convcon
from .forms import PostForm

def post_list(request):
    posts = Convcon.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'phrasebook/post_list.html', {'posts': posts})

def post_new(request):
    form = PostForm()
    return render(request, 'phrasebook/post_edit.html', {'form': form})


def reverse_list(request):
    posts = Convcon.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'phrasebook/reverse_list.html', {'posts': posts})
