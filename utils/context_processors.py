from django.shortcuts import render
from teaching.models import Subject


def subjects_all(request):
    subjects = Subject.objects.all()
    return {'subjects_all': subjects}