from django.shortcuts import render
from rest_framework import generics
from .models import Men
from .serializers import MenSerializer


class MenView(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer

# Create your views here.
