from django.shortcuts import render
def member(request,member_id) :
	response = "hello, your memberid is %s." 
	return HttpResponse(response % member_id)
# Create your views here.
