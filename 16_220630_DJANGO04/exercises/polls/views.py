from django.shortcuts import render, redirect
from polls.models import Article
# Create your views here.

def survay_home(request):
    survay_all = Article.objects.all().order_by("-pk")
    context = {
        "survay":survay_all
    }
    return render(
        request,
        "survay_html/index.html",
        context,
    )

def survay_create(request):
    if request.method == "POST":
        new_survay = Article()
        new_survay.age = request.POST.get("age")
        new_survay.sex = request.POST.get("sex")
        new_survay.residence = request.POST.get("residence")
        new_survay.residential_suggestions = request.POST.get("residential_suggestions")
        new_survay.save()

        return redirect("/survay_urls/home")
    
    elif request.method == "GET":
        return render(request, "survay_html/create.html")
    