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
    # num11 = request.GET.get('num1','0')
    # # num11 = request.GET['num1'    ]
    # num22 = request.GET.get('num2','0')
    # num = int(num11) + int(num22)


    str = request.GET.get('text',"error")
    id1 = request.GET.get('id1','off')
    id2 = request.GET.get('id2','off')
    id3 = request.GET.get('id3','off')
    id4 = request.GET.get('id4','off')
    id5 = request.GET.get('id5','off')

    if id1 == "on":

        p = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        a = " "
        for i in str:
            if i not in p :
                a=a+i     
        #  data = { 'num':num,'a':a}
        data = {'a':a}
        return render(request,'remove.html',data)
    elif id2 == "on":
        a = ""
        for char in str:
            a = a + char.upper()

        data = { 'a':a }
        return render(request,'remove.html',data)    
    elif id3 == "on":
        a = ""
        for char in str:
            if char != '\n':
                a = a + char
        data = { 'a':a }
        return render(request,'remove.html',data)   
    elif id4 == "on":
        a=""
        f=0
        # for i,char in enumerate(str):
        #     if str[i] == ' ' and  str[i+1] !== ' ':
        #         pass
        #     else:
        #         a=a+char
        # data = {'a':a}
        # return render(request,'remove.html',data) 

        for char in str:
            if (char==' ' and f==0): 
                a=a+char
                f=1
            elif char!=' ': 
                a=a+char
                f=0
        data = {'a':a}
        return render(request,'remove.html',data)  
    elif id5 == 'on':
        a=0
        for i in str:
            a=a+1
        data = {'a':a}
        return render(request,'remove.html',data)              
    else:
         return render(request,'remove.html')



    