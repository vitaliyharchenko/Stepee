from django.shortcuts import render
from models import Subject, Grade, Chapter

# Create your views here.
def subjects(request):
    args = {'subjects': Subject.objects.all()}
    return render(request, 'subjects.html', args)


def subject(request, subject_id):
    sub = Subject.objects.get(id=subject_id)
    args = {'subject': sub,
            'grades': Grade.objects.all(),
            'dict': sub.getchapters()}
    return render(request, 'subject.html', args)


def chapter(request, chapter_id):
    args = {'chapter': Chapter.objects.filter(id=chapter_id)}
    return render(request, 'chapter.html', args)


def paragraph(request):
    args = {}
    return render(request, 'paragraph.html', args)