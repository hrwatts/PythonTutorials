from django.shortcuts import render

from django.http import HttpResponse


#since this is a web server application you'll need to be aware of responses and such
#that aren't the same on normal computers

#also note that this "index" method is serving up the webpage. 
#A very basic one with solely a sentence
#all you need to do now is map an address to it (URL)
def index(request):
	#this is what will happen if the method index is run with a HttpRequest
	#it will give a HttpResponse
	#HttpResponse is actually going to generate an HTML page for display based on this
	#so things like < and > are not going to go over very well...
	response = "Hello, world! You're at the polls index. Request: " + str(request)[1:-1]
	return HttpResponse(response)



