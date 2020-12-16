from django.urls import path
from .views import *

app_name = 'conversion'
urlpatterns = [
    path('jtop/', jtop, name="jtop"),
    path('convert/', convert, name="convert"),
]