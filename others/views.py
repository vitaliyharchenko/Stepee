# coding=utf-8
from django.shortcuts import render
from teaching.models import Subject


# Create your views here.
def index(request):
    args = {'subjects': Subject.objects.all()}
    return render(request, 'index.html', args)