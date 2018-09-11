from django.contrib import admin
from .models import Student, Teacher, Class, Quiz, Question, Answer, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2

class AnswerInLine(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)
    inlines = [AnswerInLine, ChoiceInLine]


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'avg_mark')
    search_fields = ('id', 'first_name')
    ordering = ('first_name',)
    list_display_links = list_display


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject')
    search_fields = ('id', 'first_name')
    ordering = ('first_name',)
    list_display_links = list_display


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class)
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)

