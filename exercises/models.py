# coding=utf-8
from django.db import models
from django.utils import timezone
from teaching.models import Partition, Subject, Grade, Chapter, Lesson, Paragraph
from customuser.models import User


class Exercise(models.Model):
    value = models.IntegerField()  # оценка за выполнение
    subjects = models.ManyToManyField(Subject, blank=True)
    grades = models.ManyToManyField(Grade, blank=True)
    chapters = models.ManyToManyField(Chapter, blank=True)
    lessons = models.ManyToManyField(Lesson, blank=True)
    paragraphs = models.ManyToManyField(Paragraph, blank=True)
    is_test = models.BooleanField()
    is_active = models.BooleanField()
    text = models.TextField()
    answer = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return self.text[:50]


class TestOption(models.Model):
    class Meta():
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    exercise = models.ForeignKey(Exercise)
    option_text = models.CharField(max_length=300)
    is_true = models.BooleanField()


class ControlResult(models.Model):
    user = models.ForeignKey(User)
    partition = models.ForeignKey(Partition)
    date = models.DateField(default=timezone.now)
    score = models.IntegerField(null=True, blank=True)
    max_score = models.IntegerField()


class ExerciseResult(models.Model):
    control = models.ForeignKey(ControlResult)
    exercise = models.ForeignKey(Exercise)
    answer = models.CharField(max_length=300, blank=True)
    selected_option = models.ForeignKey(TestOption)