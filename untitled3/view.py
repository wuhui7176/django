from django.http import HttpResponse

from django.http import HttpResponse
from django.shortcuts import render_to_response


def hello(request):
    return HttpResponse("Hello world ! ")


def search_form(request):
    request.GET['q']
    return render_to_response('test.html')

def search1(request):
    print request.GET['q']
    return render_to_response('test.html')