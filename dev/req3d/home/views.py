from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from appform.models import Articles
from appform.forms import ArticlesForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib.auth.decorators import user_passes_test

def index(request):
    return render(request, "home/index.html")

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required(login_url='/oauth2/login')
def profile(request):
    data = Articles.objects.filter(user_id=request.user.sub)
    forms = [ArticlesForm(instance=obj) for obj in data]
    send_data = zip(data, forms)
    context = {'data': data, 'send_data': send_data}
    return render(request, "home/profile.html", context)

@login_required(login_url='/oauth2/login')
def delete_request(request, pk):
    card = get_object_or_404(Articles, pk=pk)
    if request.method == 'POST' and is_ajax(request=request):
        if request.user.sub == card.user_id:
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
            instance.user_id = request.user.sub
            instance.save()
            return JsonResponse({'success': True}, status=200)
        else:
            return JsonResponse({'success': False,'error_msg':form.errors,'error_code':'400'})
    else:
        return JsonResponse({'success': False,'error_msg':'invalid_request','error_code':'403'})

@user_passes_test(lambda u: u.is_admin, login_url='/profile')
def card(request):
    form = ArticlesForm()
    data = Articles.objects.all()
    return render(request, "home/card.html", {'data': data, 'form': form})

@login_required(login_url='/oauth2/login')
def update_admin(request):
    or_id = request.POST.get('order_id')
    or_id = int(or_id)
    data_form = get_object_or_404(Articles, id=or_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        new_comment = request.POST.get('comment')
        data_form.status = new_status
        data_form.comment = new_comment
        data_form.save()
        return redirect('card')
    else:
        return render(request, 'home.html')


@login_required(login_url='/oauth2/login')
def delete_admin(request, card_id):
    card = get_object_or_404(Articles, id=card_id)
    card.delete()
    return redirect('card')

@login_required(login_url='/oauth2/login')
def update_card_status(request):
    if request.method == 'POST':
        card_id = request.POST.get("cardId")
        new_status = request.POST.get("newStatus")
        data_form = get_object_or_404(Articles, id=card_id)
        data_form.status = new_status
        my_dict = {'id': card_id, 'status': new_status}
        data_form.save()
        return JsonResponse({'success': True, 'data': my_dict})
    
    