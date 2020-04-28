from django.urls import include, path
from . import api

urlpatterns = [
    path('search/', api.search,),
]
