from django.shortcuts import render
from .models import *
from .forms import *


def forum(request):
    topics = ForumTopic.objects.all()
    context = {'topics': topics}
    return render(request, 'forum.html', context)
