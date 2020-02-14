# Register your models here.

from django.contrib import admin

from .models import Choice, Question, Feature

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,                 {'fields':['question_text']}),
            ('Date information',   {'fields':['pub_date'], 'classes':['collapse']}),
            ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']

class FeatureAdmin(admin.ModelAdmin):

    list_display = ('feature_text')


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice) 

admin.site.register(Feature)
