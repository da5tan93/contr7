from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Question, Choice
from webapp.forms import QuestionForm

def index_view(request, *args, **kwargs):
    questions = Question.objects.filter().order_by('-pub_date')
    choices = Choice.objects.all()
    return render(request, 'index.html', context={
        'questions': questions,
        'choices': choices
    })
def question_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    choice = get_object_or_404(Choice, pk=pk)
    return render(request, 'Poll.html', context={
        'question': question,
        'choice': choice
    })


def question_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = Question.objects.create(
                poll=form.cleaned_data['poll'],
                choice=form.cleaned_data['choice'],
            )

            return redirect('question_view', pk=question.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def question_update_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'GET':
        form = QuestionForm(data={
            'poll': question.poll
        })
        return render(request, 'update.html', context={'form': form, 'question': question})
    elif request.method == 'POST':
        question.poll = request.POST.get('poll')
        question.save()
        return redirect('question_view', pk=question.pk)


def question_delete_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'question': question})
    elif request.method == 'POST':
        question.delete()
        return redirect('index')
