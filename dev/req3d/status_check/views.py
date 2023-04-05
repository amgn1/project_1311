from django.shortcuts import render, get_object_or_404
from django.http import Http404
from appform.models import Articles

def status_check(request):
    if request.GET.get("order_number"):
        try:
            order_number = request.GET.get("order_number")
            order = get_object_or_404(Articles, number=order_number)
            status = order.status
            return render(request, "status_check/status_check.html", {"order_number": order_number, "status": status})
        except Http404:
            return render(request, "status_check/status_check.html", {"order_number": order_number, "status": "Заказа не существует"})
    else:
        return render(request, "status_check/status_check.html")

