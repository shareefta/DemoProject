from django.urls import path
from . import views

app_name='srch_app'
urlpatterns=[
    path('',views.SearchResult,name='SearchResult'),
]