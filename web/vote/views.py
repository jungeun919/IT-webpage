from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .forms import QuestionForm, ChoiceForm
from datetime import datetime

# Create your views here.
def vote_list(request):
    questions = Question.objects.all()
    return render(request, 'question.html', {'questions':questions})

def vote_detail(request, question_id):
    ques = get_object_or_404(Question, id=question_id)
    return render(request, 'ques_detail.html', {'ques':ques})

def vote(request):
    if request.method == "POST":
        choice_id = request.POST.get('choice')
        choice = get_object_or_404(Choice, id=choice_id)
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('vote_result', args=(choice.q.id,)))

def vote_result(request, question_id):
    ques = get_object_or_404(Question, id=question_id)
    return render(request, 'vote_result.html', {'ques':ques})

def q_register(request):
    if request.method == "GET":
        form = QuestionForm()
        return render(request, 'q_register.html', {'form':form})

    elif request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.date = datetime.now()
            q.save()
            return HttpResponseRedirect(reverse('vote_list'))

def q_delete(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    q.delete()
    return HttpResponseRedirect(reverse('vote_list'))

def c_register(request):
    if request.method == "GET":
        form = ChoiceForm()
        return render(request, 'c_register.html', {'form':form})

    elif request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            c = form.save()
            return HttpResponseRedirect(reverse('vote_detail', args=(c.q.id,)))
        else:
            return render(request, 'c_register.html', {'form':form, 'error':'유효하지 않은 값입니다.'})

def c_delete(request, choice_id):
    c = get_object_or_404(Choice, id=choice_id)
    c.delete()
    return HttpResponseRedirect(reverse('vote_detail', args=(c.q.id,)))