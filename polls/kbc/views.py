from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from models import Question, Choice

# Create your views here.

def Polls(request):
    # result = ""
    # for q in Question.objects.all():
    #     result += q.question + "<br><ol><li>"
    #     result += '</li><li>'.join([c.choice for c in q.choices.all()]) + '</li></ol><br><br>'
    q = Question.objects.all()
    return render_to_response('kbc/question.html', {'questions' : q})
