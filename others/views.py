# coding=utf-8
from django.shortcuts import render
from teaching.models import Subject


# Create your views here.
def index(request):
    user = request.user
    args = {}
    # в этом блоке формируем массив предметов с их статусами
    if user.is_authenticated():
        args['joined_subjects'] = Subject.getjoinedsubjects(user)
        args['other_subjects'] = Subject.getothersubjects(user)
    else:
        args['other_subjects'] = Subject.getothersubjects(None)
    return render(request, 'index.html', args)