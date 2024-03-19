
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PDFDocumentViewSet, ExtractedDataViewSet

router = DefaultRouter()
router.register(r'pdf_documents', PDFDocumentViewSet)
router.register(r'extracted_data', ExtractedDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
