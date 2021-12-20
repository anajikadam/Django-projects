from django.urls import path

# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     UserPostListView
# )
from . import views

urlpatterns = [
    path('', views.home, name='project-home'),
    path('about/', views.about, name='project-about'),
    path('project1/', views.project1, name='project-project1'),
    path('people/', views.people, name='project-people'),
    path('country/', views.country, name='project-country'),
    path('peoples/', views.peoples, name='project-peoples'),
    path('countryList/', views.countryList, name='project-countryList'),
    path('project2/', views.project2, name='project-project2'),
    path('english/', views.english, name='project-english'),
    path('engToMarathi/', views.englishTomar, name='project-engtomar'),
    path('project3/', views.project3, name='project-project3'),
    path('project4/', views.project4, name='project-project4'),
]
