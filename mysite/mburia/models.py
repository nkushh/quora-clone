from django.db import models

# Create your models here.

class Question_categorie(models.Model):
	category_name = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category_name

class Mburia_question(models.Model):
	account = models.ForeignKey('auth.User')
	category = models.ForeignKey(Question_categorie)
	question_title = models.CharField(max_length=250)
	question_body = models.TextField()
	date_asked = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.question_title

class Mburia_answer(models.Model):
	question = models.ForeignKey(Mburia_question)
	answer_account = models.ForeignKey('auth.User')
	answer_text = models.TextField()
	date_answered = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.answer_text

class Answer_vote(models.Model):
	answer = models.ForeignKey(Mburia_answer)
	voting_account = models.ForeignKey('auth.User')
	vote = models.CharField(max_length=20)

	def __str__(self):
		return self.vote
