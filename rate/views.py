from django.shortcuts import render, get_object_or_404, redirect
from .models import Rate
from .forms import RateForm

def readAll(req, res):
    rates = Rate.objects.all()
    return render(req, 'rate/list.html', {'rates':rates})

def create(req, res):
    if req.method == "POST":
        form = RateForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('rate_list')
    else:
        form = RateForm()
    return render(req, 'rate/create.html', {"form":form})