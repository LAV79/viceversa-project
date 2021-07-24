from django.shortcuts import render

def home(rq):
	return render(rq,'home.html')

def reverse(rq):
	txt=rq.GET['message']
	# print(txt)
	return render(rq,'reverse.html',{'txt':txt[::-1]})
