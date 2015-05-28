from django.shortcuts import render, redirect
from models import Exercise, TestOption


# Create your views here.
def exercise(request, exercise_id):
    ex = Exercise.objects.get(id=exercise_id)
    args = {'exercise': ex}
    if ex.is_active:
        if ex.is_test:
            args['options'] = TestOption.objects.filter(exercise=ex)
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'exercise.html', args)