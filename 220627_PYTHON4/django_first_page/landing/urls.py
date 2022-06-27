from django.urls import path #

from landing import views #


urlpatterns = [ #
    path("home/", views.landing), # 사용자 주소, 돌려주고 싶은 함수가 두번째
    path("resume/", views.resume),
    path("project/", views.project),
]


# def css01(request):
#     return render(request, "landing/01_css-quiz/css-quiz-1.html")
# def css02(request):
#     return render(request, "landing/01_css-quiz/css-quiz-2.html")
# def css03(request):
#     return render(request, "landing/01_css-quiz/css-quiz-3.html")
# def css04(request):
#     return render(request, "landing/01_css-quiz/css-quiz-4.html")
# def flex01(request):
#     return render(request, "landing/02_flex-quiz/flex-quiz-1.html")
# def flex02(request):
#     return render(request, "landing/02_flex-quiz/flex-quiz-2.html")
# def position01(request):
#     return render(request, "landing/03_position-quiz/position-quiz-1.html")
# def position02(request):
#     return render(request, "landing/03_position-quiz/position-quiz-2.html")
# def position03(request):
#     return render(request, "landing/03_position-quiz/position-quiz-3.html")