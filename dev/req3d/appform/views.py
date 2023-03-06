from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import ArticlesForm
from .models import Articles
import requests

def appform_view(request):
    if request.method == 'POST':
        mail = request.POST['mail']
        name = request.POST['name']
        if mail and name:
            data = Articles(mail=mail, name=name)
            data.save()
            return render(request,'home/index.html')
    else:
        form = ArticlesForm()
        context = {'form': form}
        return render(request, "appform/appform.html", context)


