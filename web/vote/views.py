from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http.response import HttpResponseRedirect
from django.urls import reverse

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