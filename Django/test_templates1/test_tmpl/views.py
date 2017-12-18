from django.shortcuts import render

# Create your views here.

def home(request):
    # # 示例一:显示一个定义好的html主页
    # return render(request, 'home.html')

    # # 示例二:显示一个基本的字符串在网页上
    # string = u"我在学习Django，用它来建网站"
    # return render(request, 'home.html', {'string': string})

    # 示例三:基本的 for 循环 和 List内容的显示
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'TutorialList': TutorialList})
