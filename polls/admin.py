from django.contrib import admin

from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

# reordering field
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]

# split the form up into fieldsets:
class QuestionAdmin(admin.ModelAdmin):
    #Customize the admin change list
    list_display = ["question_text", "pub_date"]

    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)