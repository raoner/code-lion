from django.shortcuts import render

# Create your views here.

def survay(request):
    return render(request, "survay-html/index.html")