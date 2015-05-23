# coding=utf-8
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def subjects(request):
    return render(request, 'subjects.html')


def subject(request):
    return render(request, 'subject.html')


def chapter(request):
    return render(request, 'chapter.html')


def paragraph(request):
    return render(request, 'paragraph.html')