from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.

#cookie和session设置练习2233
def index(request):
    #获取cookie
    cookie=request.COOKIES
    context={'user':'liuchang',"cookie":cookie}
    print(cookie)

    return render(request,'user/index.html',context)

def login(request):
    Response1=HttpResponse()
    a1=request.GET['a']
    #设置session
    session=request.session['uname']='liuchanggege'
    print(type(session))
    print(session)
    context={'session':session,'b':a1}
    #设置cookie
    t1=Response1.set_cookie('hhqerhkeq','hhaha')
    print(type(t1))
    return render(request,'user/login.html',context)
    #return Response1

#重定向练习
def Redirect1(request):
    return HttpResponseRedirect('Redirect2')

def Redirect2(request):
    if request.COOKIES['hhq']=='hhaha1':
        return render(request,'user/Redirect2.html',context={'hi':'我是转向来的页面'})
    else:
        return render(request,'user/Redirect2.html',context={'hi':'异常'})

# 返回json
def testPost(request):
    content={"a":1,"b":2,"c":3}
    return HttpResponse(content=content)

