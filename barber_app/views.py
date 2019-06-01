

from django.shortcuts import render
from django.http import HttpResponse
#from .barberMember.models import Member

def index(request):
	return HttpResponse("nothing gose here...")

def member(request,member_id) :
	#response = "hello, your memberid is %s." 
	#return HttpResponse(response % member_id)
	return HttpResponse('sssssssssss')
# Create your views here.
