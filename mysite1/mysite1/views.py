from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    param = {'name':'kuldeep'}
    return render(request,'index.html',param)
    # return HttpResponse("hello home page<br> <a href='http://127.0.0.1:8000/contact'>contact</a><br><a href='http://127.0.0.1:8000/about'>about</a>")
   
def about(request):
    return HttpResponse("it is about<br> <a href='http://127.0.0.1:8000'>home</a><br><a href='http://127.0.0.1:8000/contact'>contact</a>")   

def con(request):
    return HttpResponse("it is contact <br> <a href='http://127.0.0.1:8000'>home</a><br><a href='http://127.0.0.1:8000/about'>about</a>")   

def remove(request):
    num11 = request.GET.get('num1','0')
    # num11 = request.GET['num1'    ]
    num22 = request.GET.get('num2','0')
    str = request.GET.get('text',"error")
    num = int(num11) + int(num22)
    
    p = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    a = " "
    for i in str:
        if i not in p :
              a=a+i     
    data = { 'num':num,'a':a}
    return render(request,'remove.html',data)