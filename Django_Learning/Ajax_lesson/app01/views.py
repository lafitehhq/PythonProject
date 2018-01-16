from django.shortcuts import render, HttpResponse

# Create your views here.

def index(req):
    return render(req, "index.html")



def ajax_receive(req):
    if req.method == 'Post':
        print("req.POST", req.POST)
    return HttpResponse("hello2")

# 基于Jquery的Ajax的实现
def jquery_test(req):
    return render(req, "ajax_jquery.html")

def jquery_get(req):
    print(req.GET)

    return HttpResponse("Get请求基于Jquery的Ajax的实现")