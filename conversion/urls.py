from django.urls import path
from .views import *

app_name = 'conversion'
urlpatterns = [
    path('jtop/', jtop, name="jtop"),
    path('presult/', presult, name="presult"),
    path('ptoj/', ptoj, name="ptoj"),
    path('jresult/', jresult, name="jresult"),
]