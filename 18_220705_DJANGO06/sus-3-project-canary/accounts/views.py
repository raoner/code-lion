from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def sign_up(request):
    # 로그인 한 사람 걸러내기?
    if request.user.is_authenticated:
        return redirect("accounts:logged-in")
    
    context = {}
    if request.method == "POST":
        username_input = request.POST.get("username")
        password_input = request.POST.get("password")
        password_check_input = request.POST.get("password_check")
        if username_input and \
            password_input and \
            password_check_input == password_input:

            if User.objects.filter(username=username_input).exists():
                context["error"] = "사용중인 아이디 입니다."
            else:
                new_user = User.objects.create_user(
                    username=username_input,
                    password=password_input,
                )
                auth.login(request, new_user)
                # 로그인이 자동 진행이 되게 하는 것.?
                return redirect("accounts:logged-in")
        else:
            context["error"] = "올바르지 않은 정보입니다."
    else:
        pass

    return render(request, "accounts/sign-up.html", context)


def sign_in(request):
    context = {}
    if request.method == "POST":
        username_input = request.POST.get("username")
        password_input = request.POST.get("password")
        if username_input and password_input:
            sign_in_user = auth.authenticate(
                request, 
                username=username_input, 
                password=password_input,
            )
            # 존재하는 개체를 돌려줌...
            # 클래스 객체
            if sign_in_user is not None:
                auth.login(request, sign_in_user)
                return redirect("accounts:logged-in")
                # return redirect("/")
            else:
                context["error"] = "해당하는 사용자가 없습니다."
        else:
            context["error"] = "아이디와 비밀번호를 입력해주세요."

    return render(request, "accounts/sign-in.html", context)


def logged_in(request):
    # print(request.user.is_authenticated)
    # print(request.user.username)
    context = {
        "logged_in": request.user.is_authenticated, # 지금 들어온 요청이 로그인 한 사람인지 아닌지 판단 기준이 된다.
    }
    return render(request, "accounts/logged-in.html", context)

# 로그 아웃. urls에 추가 해야 함.
def sign_out(request):
    if request.method == "POST":
        auth.logout(request)
    return redirect("accounts:logged-in")