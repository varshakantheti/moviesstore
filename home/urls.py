from django.urls import path
from . import views
"""
From Textbook:
The first argument, '', represents the URL pattern itself. In this case, it’s an empty string, indicating the root URL. This means that when the root URL of the application is accessed (localhost:8000/), it will match this path.
The second argument, views.index, refers to the view function that will handle the HTTP request. Here, views.index indicates that the index function in the views file is responsible for processing the request.
The third argument, name='home.index', is the name of the URL pattern. This name is used to uniquely identify the URL pattern and can be referenced in other parts of the Django project, such as templates or other URL patterns.
"""
urlpatterns = [
    path('', views.index, name='home.index'),
    path('about', views.about, name='home.about'),
]