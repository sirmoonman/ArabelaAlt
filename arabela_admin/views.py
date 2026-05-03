from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import Http404


def dashboard_view(request):
    return render(request, "arabela_admin/dashboard.html")


def rental_schedule_view(request):
    return render(request, "arabela_admin/calendar.html", {"page": "rental"})


def payment_verification_view(request):
    return render(request, "arabela_admin/payment-verification.html", {"page": "payment-verification"})


def security_deposits_view(request):
    return render(request, "arabela_admin/security-deposits.html", {"page": "security-deposits"})


def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username:
            return render(
                request,
                "arabela_admin/admin-login.html",
                {"error": "Please enter your username.", "username": username},
            )

        if not password:
            return render(
                request,
                "arabela_admin/admin-login.html",
                {"error": "Please enter your password.", "username": username},
            )

        authenticated_user = authenticate(request, username=username, password=password)
        if not authenticated_user:
            return render(
                request,
                "arabela_admin/admin-login.html",
                {"error": "Invalid username or password.", "username": username},
            )

        if not (authenticated_user.is_staff or authenticated_user.is_superuser):
            return render(
                request,
                "arabela_admin/admin-login.html",
                {"error": "This account has no admin access.", "username": username},
            )

        login(request, authenticated_user)
        remember_me = request.POST.get("remember_me") == "on"
        request.session.set_expiry(settings.REMEMBER_ME_AGE if remember_me else 0)
        return redirect("arabela_admin:dashboard")

    # Treat opening admin login page from the dropdown as sign-out.
    if request.user.is_authenticated:
        logout(request)
    return render(request, "arabela_admin/admin-login.html")


def page_view(request, page: str):
    allowed_pages = {
        "alerts",
        "badge",
        "basic-tables",
        "blank",
        "buttons",
        "calendar",
        "form-elements",
        "profile",
        "sidebar",
        "payment-verification",
        "security-deposits",
    }
    if page not in allowed_pages:
        raise Http404("Page not found")
    return render(request, f"arabela_admin/{page}.html")
