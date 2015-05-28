from django.contrib import admin
from models import Subject, Grade, Chapter, Lesson, Paragraph, Partition, LearningStatus

# TODO: add inline childrens classes
# class TestOptionInline(admin.StackedInline):
#     model = TestOption
#
#
# class ExerciseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'text', 'is_test', 'is_active', 'value')
#     inlines = [TestOptionInline]
#
# admin.site.register(Exercise, ExerciseAdmin)

# Register your models here.
admin.site.register(Partition)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Chapter)
admin.site.register(Lesson)
admin.site.register(Paragraph)
admin.site.register(LearningStatus)