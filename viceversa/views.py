from django.shortcuts import render

def home(rq):
	return render(rq,'home.html')

def reverse(rq):
	txt=rq.GET['message']
	# print(txt)
	return render(rq,'reverse.html',{'txt_org':txt,'txt_rev':txt[::-1],'num':len(txt.split())})
