from django.shortcuts import render
from django.http import HttpResponse
from appform.models import Articles
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "home/index.html")

@login_required(login_url='/oauth2/login')
def profile(request):
    data = Articles.objects.filter(user_id=request.user.id)
    context = {'data': data}
    return render(request, "home/profile.html", context)