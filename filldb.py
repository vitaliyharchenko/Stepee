# coding=utf-8
import sys
import os

import django


sys.path.extend(['/Dev/Stepee'])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Stepee.settings")
django.setup()

from teaching.models import Subject, Grade, Chapter, Lesson, Paragraph, LearningStatus
from exercises.models import Exercise, TestOption
from customuser.models import User

# print 'Creating superuser...'
# User.objects.create_superuser(email="harchenko.grape@gmail.com", password="4203", first_name="Vitaliy",
#                               last_name="Harchenko")

print 'Creating subjects...'
Subject.objects.create(title=u'Физика', description=u'Физика из зе бест есть жи')
Subject.objects.create(title=u'Математика' , description=u'Математика - забавная лалка')
print Subject.objects.all()

print 'Creating grades...'
Grade.objects.create(title=u'7 класс')
Grade.objects.create(title=u'8 класс')
Grade.objects.create(title=u'9 класс')
Grade.objects.create(title=u'10 класс')
Grade.objects.create(title=u'11 класс')
print Grade.objects.all()

print 'Creating chapters...'
Chapter.objects.create(title=u'Что такое физика?',
                       grade=Grade.objects.get(title=u'7 класс'),
                       subject=Subject.objects.get(title=u'Физика'))
Chapter.objects.create(title=u'Механика. Часть 1',
                       grade=Grade.objects.get(title=u'7 класс'),
                       subject=Subject.objects.get(title=u'Физика'))
Chapter.objects.create(title=u'Тепловые процессы',
                       grade=Grade.objects.get(title=u'8 класс'),
                       subject=Subject.objects.get(title=u'Физика'))
Chapter.objects.create(title=u'Электричество и магнетизм. Часть 1',
                       grade=Grade.objects.get(title=u'8 класс'),
                       subject=Subject.objects.get(title=u'Физика'))
Chapter.objects.create(title=u'Геометрическая оптика',
                       grade=Grade.objects.get(title=u'8 класс'),
                       subject=Subject.objects.get(title=u'Физика'))
print Chapter.objects.all()

print 'Creating lessons...'
Lesson.objects.create(title=u'День 1. Температурные шкалы',
                      chapter=Chapter.objects.get(title=u'Что такое физика?'))
Lesson.objects.create(title=u'День 2. Тепловые процессы',
                      chapter=Chapter.objects.get(title=u'Что такое физика?'))
Lesson.objects.create(title=u'День 3. Вата',
                      chapter=Chapter.objects.get(title=u'Что такое физика?'))
Lesson.objects.create(title=u'День 4. Цветочки',
                      chapter=Chapter.objects.get(title=u'Что такое физика?'))
print Lesson.objects.all()

print 'Creating paragraphs...'
Paragraph.objects.create(title=u'Температура',
                         lesson=Lesson.objects.get(title=u'День 1. Температурные шкалы'))
Paragraph.objects.create(title=u'Кельвин',
                         lesson=Lesson.objects.get(title=u'День 1. Температурные шкалы'))
Paragraph.objects.create(title=u'Цельсий',
                         lesson=Lesson.objects.get(title=u'День 1. Температурные шкалы'))
Paragraph.objects.create(title=u'Клапейрон',
                         lesson=Lesson.objects.get(title=u'День 1. Температурные шкалы'))
print Paragraph.objects.all()

print 'Creating exercises...'
Exercise.objects.create(value=1, is_test=True, text=u'На ветке сидело 10 птиц, 3 улетели. Сколько осталось?', is_active=True)
TestOption.objects.create(exercise=Exercise.objects.get(is_test=True), option_text='7', is_true=True)
TestOption.objects.create(exercise=Exercise.objects.get(is_test=True), option_text='5', is_true=False)
TestOption.objects.create(exercise=Exercise.objects.get(is_test=True), option_text='6', is_true=False)
Exercise.objects.create(value=1, is_test=False, text=u'Найдите плотность воды. Ответ выразите в кг\м^3', is_active=True)
print Exercise.objects.all()

print 'Creating learning statuses...'
LearningStatus.objects.create(partition=Subject.objects.get(title=u'Физика'), passing_status='closed', user=User.objects.get(), score=40, max_score=60)