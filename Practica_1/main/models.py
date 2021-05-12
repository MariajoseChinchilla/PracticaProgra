from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your models here.

class UploadedFiles(models.Model):
    title = models.CharField(max_length=100)
    p2 = models.FileField(upload_to='archivos/p2/')

    def __str__(self):
        return self.title
