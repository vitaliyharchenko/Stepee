# coding=utf-8
from django.db import models
from django.core.exceptions import ObjectDoesNotExist


# Главный класс для любого раздела (предмет, класс, глава, урок, параграф)
class Partition(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.title

    @property
    def getstatus(self):
        return 'cnfnec'


class NextPartitionRelation(models.Model):
    parent = models.ForeignKey(Partition, related_name='parent')
    children = models.ForeignKey(Partition, related_name='children')


class Subject(Partition):
    class Meta():
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    description = models.TextField(default='')

    def __unicode__(self):
        return self.title

    @property
    def getchapters(self):
        grades = Grade.objects.all()
        count = grades.count()
        chapters = {}
        for i in range(0, count):
            result = Chapter.objects.filter(subject=self, grade=grades[i])
            if result.count() > 0:
                chapters[grades[i]] = result
        return chapters

    # TODO: refactor method
    @staticmethod
    def getjoinedsubjects(user):
        subjects = Subject.objects.all()
        count = subjects.count()
        arr_joined = {}
        for i in range(0, count):
            try:
                learning_status = LearningStatus.objects.get(partition=subjects[i], user=user)
                status = learning_status.passing_status
                if status == 'win' or status == 'work' or status == 'lose':
                    arr_joined[subjects[i]] = status
            except ObjectDoesNotExist:
                pass
        return arr_joined

    # TODO: refactor method
    @staticmethod
    def getothersubjects(user):
        subjects = Subject.objects.all()
        count = subjects.count()
        arr_others = {}
        for i in range(0, count):
            try:
                learning_status = LearningStatus.objects.get(partition=subjects[i], user=user)
                status = learning_status.passing_status
                if status == 'win' or status == 'work' or status == 'lose':
                    pass
                else:
                    arr_others[subjects[i]] = status
            except ObjectDoesNotExist:
                arr_others[subjects[i]] = 'closed'
        return arr_others


class Grade(Partition):
    class Meta():
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __unicode__(self):
        return self.title


class Chapter(Partition):
    class Meta():
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    grade = models.ForeignKey(Grade)
    subject = models.ForeignKey(Subject)

    def __unicode__(self):
        return u'{} - {} - {}'.format(self.subject, self.grade, self.title)
        # return self.title


class Lesson(Partition):
    class Meta():
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    chapter = models.ForeignKey(Chapter)

    def __unicode__(self):
        return self.title


class Paragraph(Partition):
    class Meta():
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы'

    lesson = models.ForeignKey(Lesson)

    def __unicode__(self):
        return self.title


# Модель для статуса прохождения раздела (не приступил, приступил, завалил, недоступно итд)
# TODO: при завершении
class LearningStatus(models.Model):
    class Meta():
        verbose_name = 'Статус обучения'
        verbose_name_plural = 'Статусы обучения'

    # объявление без импорта - избавление от циклического импорта
    user = models.ForeignKey('customuser.User')
    partition = models.ForeignKey(Partition)
    NOTHING = 'available'
    BEGINNER = 'work'
    LOSER = 'lose'
    MASTER = 'win'
    CLOSED = 'closed'
    PASSING_CHOICES = (
        (NOTHING, 'Доступно'),
        (BEGINNER, 'В работе'),
        (LOSER, 'Неудачно'),
        (MASTER, 'Завершено'),
        (CLOSED, 'Недоступно'),
    )
    passing_status = models.CharField(choices=PASSING_CHOICES, default=CLOSED, max_length=10)
    score = models.IntegerField(null=True, blank=True, default=0)
    max_score = models.IntegerField(null=True, blank=True, default=0)
    # TODO: вычисление максимального балла на лету

    def __unicode__(self):
        return u'{} - {} - {}'.format(self.user.get_full_name(), self.partition.title, self.passing_status)