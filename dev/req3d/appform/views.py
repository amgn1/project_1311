from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArticlesForm

def appform_view(request):
    form = ArticlesForm()
    context = {'form': form}
    return render(request, "appform/appform.html", context)