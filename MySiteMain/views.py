#coding: utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from datetime import datetime
from models import Blog

def index(request):
    return render(request,'index.html')
def cal(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse("a+b="+str(c))
def add2(req,a,b):
    c=int(a)+int(b)
    return HttpResponse("Add2:a+b="+str(c))
def homepage(request):
    string="张三"
    return render(request, 'homepage.html',{'string':string})
def currenttime(request):
    now = datetime.now()
    return render_to_response(now);
def getblogs(request):
    contxt = {'blogs':Blog.objects.all().order_by('-created')}
    return render(request,'blogs_list.html',contxt)
