from django.shortcuts import render
from .models import Problems, Solutions, TestCases


def prob_list(request):
    problem = Problems.objects.all()
    context = {
        'prob_list': problem
    }
    return render(request, "judge/prob_list.html", context)
