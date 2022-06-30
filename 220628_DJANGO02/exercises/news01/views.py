from django.shortcuts import render

# Create your views here.
def news01(request):
    return render(request,"landing/index.html")