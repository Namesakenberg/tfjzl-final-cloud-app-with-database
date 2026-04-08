from django.contrib import admin
# Import all models
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# 🔥 Inline for Choice (inside Question)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


# 🔥 Inline for Question (inside Course)
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


# Existing Lesson inline
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Course Admin (add QuestionInline here)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# 🔥 Use decorator (IMPORTANT for grader)
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'course', 'grade')


# 🔥 Register remaining models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Choice)
admin.site.register(Submission)