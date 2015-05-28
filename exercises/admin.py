from django.contrib import admin
from models import Exercise, TestOption


class TestOptionInline(admin.StackedInline):
    model = TestOption


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'is_test', 'is_active', 'value')
    inlines = [TestOptionInline]

admin.site.register(Exercise, ExerciseAdmin)