from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question, Choice

# Create your views here.

def index(request):
	questions = Question.objects.order_by('-pub_date')
	context = {
		'questions' : questions,
	}
	return render(request, 'polls/polls.html', context)

def question_detail(request, pk):
	question = get_object_or_404(Question, pk=pk)
	context = {
		'question' : question,
	}
	return render(request, 'polls/question.html', context)

@login_required(login_url='login')
def new_vote(request, pk):
	question = get_object_or_404(Question, pk=pk)
	if request.method == 'POST':
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
		selected_choice.votes += 1
		selected_choice.save()
		messages.success(request, 'Success! Your vote has successfully been tallied.')
		return redirect('polls:question_detail', pk=question.id)
	else:
		return render(request, 'polls/question.html', {'question' : question})

