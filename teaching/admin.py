from django.contrib import admin
from models import Subject, Grade, Chapter, Lesson, Paragraph, Partition, LearningStatus


# TODO: add inline childrens classes

class LessonsInline(admin.StackedInline):
    model = Lesson
    fk_name = 'chapter'


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'grade', 'subject')
    inlines = [LessonsInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'chapter', 'subject')


# Register your models here.
admin.site.register(Partition)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Lesson)
admin.site.register(Paragraph)
admin.site.register(LearningStatus)