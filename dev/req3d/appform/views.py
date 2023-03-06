from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import ArticlesForm

def appform_view(request):
    print("hello world")
    form = ArticlesForm()
    context = {'form': form}
    return render(request, "appform/appform.html", context)
def add_data(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            # data = ArticlesForm()
            # data.Meta.widgets['mail'] = form.cleaned_data.get['mail']
            form.save()
            return redirect('add_data')
    else:
        form = ArticlesForm()
    return render(request, 'appform/appform.html', {'form': form})
    # return render(request, 'appform/appform.html', {'form': form})

def success(request):
    return render(request, 'success.html')