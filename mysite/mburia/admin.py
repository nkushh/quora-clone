from django.contrib import admin

from .models import Question_categorie, Mburia_question, Mburia_answer, Answer_vote

# Register your models here.
admin.site.register(Question_categorie)
admin.site.register(Mburia_question)
admin.site.register(Mburia_answer)
admin.site.register(Answer_vote)
