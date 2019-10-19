from django.contrib import admin
from webapp.models import Choice, Question, Answer


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['poll']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('pk', 'poll', 'pub_date')

admin.site.register(Question, QuestionAdmin)