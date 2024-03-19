#from django.db import models

# Create your models here.
from django.db import models

class PDFDocument(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='pdf_files/')

class ExtractedData(models.Model):
    pdf = models.ForeignKey(PDFDocument, on_delete=models.CASCADE)
    content = models.TextField()
