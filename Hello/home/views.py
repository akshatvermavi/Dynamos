from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is homepage")
def about(request):
    return HttpResponse("This is about page")
def services(request):
    return HttpResponse("This is service page")
def contact(request):
    return HttpResponse("This is contact page")
