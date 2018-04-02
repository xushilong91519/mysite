from django.urls import path
from .views import homepage,showpost,homepage_sorted

app_name='mysite'
urlpatterns=[
    path('<str:Slug>/',showpost,name='showpost'),
]

