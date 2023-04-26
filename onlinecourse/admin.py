from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class ChoiceInLine(admin.TabularInline):
    model = Choice

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

#Create QuestionAdmin and ChoiceAdmin to customize forms
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display = ['id','question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice_text', 'is_correct']

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
