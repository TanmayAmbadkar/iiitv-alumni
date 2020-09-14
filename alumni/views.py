from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView
from rest_framework import viewsets

from alumni.serializers import *
from alumni.models import *


class AlumniViewSet(viewsets.ModelViewSet):
    queryset = Alumni.objects.all().order_by('rollno')
    serializer_class = AlumniSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
