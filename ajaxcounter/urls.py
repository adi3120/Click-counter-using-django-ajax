from django.urls import path
from . import views

app_name='ajaxcounter'
urlpatterns=[
	path('',views.index,name="index")
]