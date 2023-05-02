from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import ArticlesForm
from .models import Articles
import requests
from django.contrib.auth.decorators import login_required

@login_required(login_url='/oauth2/login')
def appform_view(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        context = {'form': form}
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user.sub
            instance.save()

            return redirect('/')
    else:
        form = ArticlesForm()
        context = {'form': form}
    return render(request, "appform/appform.html", context)
