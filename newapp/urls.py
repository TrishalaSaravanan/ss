from django.urls import path
from . import views

urlpatterns = [
    path('page/',views.indexhtml, name='indexhtml'),
    path('page/indexhtml1/',views.indexhtml1, name='indexhtml1'),
    path('page/indexhtml1/indexhtml2/',views.indexhtml2, name='indexhtml2'),
]