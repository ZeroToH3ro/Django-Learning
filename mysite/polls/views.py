from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
# Create your views here.
def index(request):
    myname = "Minh"
    assets = ["phone", "laptop", "plane", "gold"]
    context = {"name": myname, "assets": assets}
    
    return render(request, "polls/index.html", context)


def viewlist(request):
    list_question = Question.objects.all()
    context = {"lst_quest": list_question}
    return render(request, "polls/question_list.html", context)


def detail_view(request, question_id):
    q = Question.objects.get(pk = question_id)
    context = {"question": q}
    return render(request, "polls/detail_question.html", context) 

def vote(request, question_id):
    q = Question.objects.get(pk = question_id)

    try:
        data = request.POST["choice"]
        c = q.choice_set.get(pk = data)
    except:
        HttpResponse("No choice")

    c.vote += 1
    c.save()

    return render(request, "polls/result.html", {"question": q})