from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="landingpg"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.sme_dashboard, name="sme_dashboard"),

]
