from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count
from django.shortcuts import render, redirect, get_object_or_404

from polls.models import Question, Choice
from .models import Question_categorie, Mburia_question, Mburia_answer, Answer_vote

# Create your views here.
def index(request):
	questions = Mburia_question.objects.all().order_by('-date_asked')
	categories = Question_categorie.objects.all()
	context = {
		'questions' : questions,
		'categories' : categories
	}
	return render(request, 'mburia/home.html', context)

def ask_question(request):
	questions = Question.objects.all()
	categories = Question_categorie.objects.all()
	context = {
		'questions' : questions,
		'categories' : categories
	}

	return render(request, 'mburia/ask.html', context)

@login_required(login_url='login')
def submit_question(request):
	if request.method == 'POST':
		category = Question_categorie.objects.get(pk=request.POST['category'])
		account = request.user
		question = Mburia_question(
				account=account, 
				category=category, 
				question_title=request.POST['question_title'], 
				question_body=request.POST['question_body']).save()

		messages.success(request, 'Success! Your query has successfully been submitted.')
		return redirect('mburia:mburia_home')
	else:
		messages.error(request, 'Error! Your query was not submitted. Try again!')
		return redirect('mburia:ask_question')

def category_questions(request, pk):
	questions = Mburia_question.objects.filter(category=pk).order_by('-date_asked')
	categories = Question_categorie.objects.all()
	context = {
		'questions' : questions,
		'categories' : categories
	}

	return render(request, 'mburia/category.html', context)

def question_detail(request, pk):
	question = get_object_or_404(Mburia_question, pk=pk)
	categories = Question_categorie.objects.all()
	up_votes = Answer_vote.objects.filter(vote="up").values('answer').annotate(up_vote = Count('id'))
	down_votes = Answer_vote.objects.filter(vote="down").values('answer').annotate(down_vote = Count('id'))
	context = {
		'question' : question,
		'categories' : categories,
		'up_votes' : up_votes,
		'down_votes' : down_votes,
	}
	return render(request, 'mburia/question.html', context)

@login_required(login_url='login')
def submit_answer(request, pk):
	question = Mburia_question.objects.get(pk=pk)

	if request.method=='POST':
		answer = Mburia_answer(
				question=question, 
				answer_account=request.user, 
				answer_text=request.POST['answer_text']).save()
		messages.success(request, 'Success! Your answer has successfully been submitted.')
		return redirect('mburia:question_detail', pk=pk)
	else:
		messages.error(request, 'Error! Your answer has not been submitted.')
		return redirect('mburia:question_detail', pk=pk)


@login_required(login_url='login')
def up_answer_vote(request, pk, question):
	answer = Mburia_answer.objects.get(pk=pk)
	voting_account = request.user
	vote = 'up'
	if not(Answer_vote.objects.filter(answer=pk).filter(voting_account=voting_account).exists()):
		votes = Answer_vote(answer=answer, voting_account=request.user, vote=vote).save()
		messages.success(request, 'Success! Your vote has been tallied.')
		return redirect('mburia:question_detail', pk=question)
	else:
		messages.warning(request, 'Error! Your vote has not been tallied. You already voted')
		return redirect('mburia:question_detail', pk=question)

@login_required(login_url='login')
def down_answer_vote(request, pk, question):
	answer = Mburia_answer.objects.get(pk=pk)
	voting_account = request.user
	vote = 'down'

	if not(Answer_vote.objects.filter(answer=pk).filter(voting_account=voting_account).exists()):
		votes = Answer_vote(answer=answer, voting_account=request.user, vote=vote).save()
		messages.success(request, 'Success! Your vote has been tallied.')
		return redirect('mburia:question_detail', pk=question)
	else:
		messages.warning(request, 'Error! Your vote has not been tallied. You already voted')
		return redirect('mburia:question_detail', pk=question)





# @login_required(login_url='login')
# messages.success(request, 'Success! Your vote has successfully been tallied.')