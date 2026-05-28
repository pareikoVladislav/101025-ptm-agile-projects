from django.http import HttpResponse
from django.urls import path

from projects.views.projects import get_all_projects

urlpatterns = [
    path('', lambda request: HttpResponse('hello')),
    path('projects/',get_all_projects),
]

