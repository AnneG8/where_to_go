from django.shortcuts import render


def show_mainpage(request):
	return render(request, 'mainpage.html')
