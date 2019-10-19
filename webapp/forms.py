from django import forms
from django.forms import widgets


class QuestionForm(forms.Form):
    poll = forms.CharField(max_length=200, required=True, label='Poll', widget=widgets.Textarea)
    choice = forms.CharField(max_length=200, label='Choice')
    #answer = forms.RadioSelect()
