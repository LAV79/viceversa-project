from django.shortcuts import render

def home(rq):
	return render(rq,'home.html')

def reverse(rq):
	return render(rq,'reverse.html')
