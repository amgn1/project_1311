from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from appform.models import Articles
from appform.forms import ArticlesForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from datetime import timezone, timedelta


def index(request):
    return render(request, "home/index.html")

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required(login_url='/oauth2/login')
def profile(request):
    data = Articles.objects.filter(user_id=request.user.id)
    forms = [ArticlesForm(instance=obj) for obj in data]
    send_data = zip(data, forms)
    context = {'data': data, 'send_data': send_data}
    return render(request, "home/profile.html", context)

@login_required(login_url='/oauth2/login')
def delete_request(request, pk):
    card = get_object_or_404(Articles, pk=pk)
    if request.method == 'POST' and is_ajax(request=request):
        if request.user.id == card.user_id:
            card.delete()
            return HttpResponseRedirect('/profile', status=200)
    

@login_required(login_url='/oauth2/login')
def update_request(request):
    form_id = request.POST.get('object_id')  
    form_data = get_object_or_404(Articles, pk=form_id)
    form = ArticlesForm(instance=form_data)
    print(request.META.get('HTTP_X_REQUESTED_WITH'))
    if request.method == 'POST' and is_ajax(request=request):
        form = ArticlesForm(request.POST, request.FILES, instance=form_data)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user.id
            instance.save()
            return JsonResponse({'success': True}, status=200)
        else:
            return JsonResponse({'success': False,'error_msg':form.errors,'error_code':'400'})
    else:
        return JsonResponse({'success': False,'error_msg':'invalid_request','error_code':'403'})
    
