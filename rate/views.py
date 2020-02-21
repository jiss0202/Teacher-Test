from django.shortcuts import render, get_object_or_404, redirect
from .models import Rate
from .forms import RateForm

def readAll(req):
    rates = Rate.objects.all().order_by("-created_at")
    return render(req, 'rate/list.html', {'rates':rates})

def create(req):
    if req.method == "POST":
        form = RateForm(req.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = req.user
            rate.save()
            return redirect('rate_list')
    else:
        form = RateForm()
    return render(req, 'rate/create.html', {"form":form})

def detail(req, rate_id):
    rate = get_object_or_404(Rate, pk = rate_id )
    return render(req, 'rate/detail.html', {'rate': rate})

def edit(req):
    return render(request, 'rate/edit.html')

def update(req, rate_id):
    rate = get_object_or_404(Rate, pk = rate_id )
    if req.method == "POST":
        form = RateForm(req.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = req.user
            rate.save()
            return redirect('detail', rate_id=rate.pk)
    else:
        form = RateForm()
        return render(req, 'rate/edit.html', {"form":form})