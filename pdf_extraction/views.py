#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import PDFDocument, ExtractedData
from .serializers import PDFDocumentSerializer, ExtractedDataSerializer
from pdfminer.high_level import extract_text

class PDFDocumentViewSet(viewsets.ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer

    def perform_create(self, serializer):
        serializer.save()

        # Extract content from uploaded PDF and save to database
        pdf_instance = serializer.instance
        content = extract_text(pdf_instance.file)
        ExtractedData.objects.create(pdf=pdf_instance, content=content)

class ExtractedDataViewSet(viewsets.ModelViewSet):
    queryset = ExtractedData.objects.all()
    serializer_class = ExtractedDataSerializer
