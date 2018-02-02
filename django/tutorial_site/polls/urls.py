from django.urls import path
from . import views #you are saying from this directory import the python file "views.py"

urlpatterns = [ #you have a method called index in views 
	#which server content, here you specify how to get
	path('', views.index, name='index'), #to that content
]

'''
after configuring the urls.py in the main tutorial_site directory
you can navigate to here using
http://127.0.0.1:8000/polls/

(having named the /polls path of the path to go to this file)

and from here it will redirect it to views.index (method index inside views)

and that's it!
'''
