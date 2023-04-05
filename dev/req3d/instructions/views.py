from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def instructions(request):
    return render(request, "instructions/instructions.html")