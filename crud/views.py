from django.shortcuts import render

# Create your views here.
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets


class  BlogModelViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer