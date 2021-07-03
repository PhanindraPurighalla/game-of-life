from django.urls import path
from . import views

urlpatterns = [
    path('careers/', views.index, name='all-careers'), # our-domain.com/careers
    path('careers/<slug:career_slug>', views.career_details, name='career-details'), # our-domain.com/careers/<dynamic-path-segment>
]