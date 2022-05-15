from django.urls import path, include
from projects import views

urlpatterns = [
    #path('<pk>/view', views.ProjectDetailView.as_view()),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    #http://localhost:8000/project181/
]