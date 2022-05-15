from django.shortcuts import render
from django.utils import timezone
from .models import Project
from django.views.generic import DetailView
#api
from rest_framework import viewsets
from .serializers import ProjectSerializer

# Create your views here.

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetailView,
             self).get_context_data(*args, **kwargs)
             
        return context