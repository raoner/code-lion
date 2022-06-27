from django.shortcuts import render

# Create your views here.

def css01(request):
    return render(request, "landing/01_css-quiz/css-quiz-1.html")
def css02(request):
    return render(request, "landing/01_css-quiz/css-quiz-2.html")
def css03(request):
    return render(request, "landing/01_css-quiz/css-quiz-3.html")
def css04(request):
    return render(request, "landing/01_css-quiz/css-quiz-4.html")
def flex01(request):
    return render(request, "landing/02_flex-quiz/flex-quiz-1.html")
def flex02(request):
    return render(request, "landing/02_flex-quiz/flex-quiz-2.html")
def position01(request):
    return render(request, "landing/03_position-quiz/position-quiz-1.html")
def position02(request):
    return render(request, "landing/03_position-quiz/position-quiz-2.html")
def position03(request):
    return render(request, "landing/03_position-quiz/position-quiz-3.html")