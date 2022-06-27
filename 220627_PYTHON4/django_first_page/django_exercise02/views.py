from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "landing/index.html")
def mail(request):
    return render(request, "landing/mail.html")
def cafe(request):
    return render(request, "landing/cafe.html")
def blog(request):
    return render(request, "landing/blog.html")
def shop(request):
    return render(request, "landing/shop.html")