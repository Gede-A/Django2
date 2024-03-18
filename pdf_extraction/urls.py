from django.urls import path
from .views import pdfExtractionView

urlpatterns = [
    path("", pdfExtractionView, "home"),
]
