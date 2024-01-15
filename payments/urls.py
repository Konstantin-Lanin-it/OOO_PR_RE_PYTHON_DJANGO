from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("item/<int:pk>", views.ItemView.as_view(), name="item"),
    path(
        "buy/<int:pk>/",
        views.SessionView.as_view(),
        name="session",
    ),
    path("cancelled/", views.CancelledView.as_view(), name="cancelled"),
    path("success/", views.SuccessView.as_view(), name="success"),
]
