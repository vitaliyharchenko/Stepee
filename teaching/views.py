from django.shortcuts import render
from models import Subject, Grade, Chapter, Lesson, Paragraph
from teaching.models import LearningStatus


# Create your views here.
def subjects(request):
    args = {'subjects': Subject.objects.all()}
    return render(request, 'subjects.html', args)


def subject(request, subject_id):
    sub = Subject.objects.get(id=subject_id)
    args = {'subject': sub,
            'dict': sub.getchapters()}
    if request.user.is_authenticated():
        learning_status = LearningStatus.objects.get(partition=sub, user=request.user)
        status = learning_status.passing_status
        score = learning_status.score
        max_score = learning_status.max_score
        args['score'] = score
        args['max_score'] = max_score
        args['score_percent'] = score*100//max_score
        args['status'] = status
    return render(request, 'subject.html', args)


def chapter(request, chapter_id):
    args = {'chapter': Chapter.objects.filter(id=chapter_id)}
    return render(request, 'chapter.html', args)


def paragraph(request, paragraph_id):
    args = {'paragraph': Paragraph.objects.filter(id=paragraph_id)}
    return render(request, 'paragraph.html', args)