from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

sign_up = CreateView.as_view(
    form_class=UserCreationForm,
    # template_name="accounts/sign_up_form.html",
    template_name="form.html",
    success_url=settings.LOGIN_URL,
)

sign_in = LoginView.as_view(
    template_name = "form.html",
)

sign_out = LogoutView.as_view(
    next_page = settings.LOGIN_URL,
)


# def sign_up(request):
#     pass

# def sign_in(request):
#     pass

# def sign_out(request):
#     pass

@login_required
def profile(request):
    return render(request, "accounts/profile.html")