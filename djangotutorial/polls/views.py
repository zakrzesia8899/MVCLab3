from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def detail(request, question_id):
    return HttpResponse("Tutaj są pytania %s." % question_id)


def results(request, question_id):
    response = "Tutaj są odpowiedzi do pytania %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Głosujesz na pytanie %s." % question_id)