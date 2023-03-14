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
        mail = request.POST['mail']
        name = request.POST['name']
        op = request.POST['op']
        course = request.POST['course']
        project_name = request.POST['project_name']
        teach_name = request.POST['teach_name']
        phone = request.POST['phone']
        dmodel = request.FILES['dmodel']
        note = request.FILES['note']
        if mail and name:
            data = Articles(mail=mail, name=name, op=op, course=course, project_name=project_name, teach_name=teach_name,phone=phone, dmodel=dmodel, note=note)
            data.save()
            return render(request,'home/index.html')
    else:
        form = ArticlesForm()
        context = {'form': form}
        return render(request, "appform/appform.html", context)
