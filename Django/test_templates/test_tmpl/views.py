from django.shortcuts import render

# Create your views here.

def home(request):
    # # 示例一:显示一个定义好的html主页
    # return render(request, 'home.html')

    # 示例二:显示一个基本的字符串在网页上
    # string = u"我在学习Django，用它来建网站"
    # return render(request, 'home.html', {'string': string})

    # 示例三:基本的 for 循环 和 List内容的显示
    # TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    # return render(request, 'home.html', {'TutorialList': TutorialList})

    # # 示例四:在模板进行 条件判断和 for 循环的详细操作
    # List = map(str, range(100))  # 一个长度为100的 List
    # return render(request, 'home.html', {'List': List})

    # 示例五:遍历字典
    # info_dict = {'site': u'维基百科', 'content': u'人类的百科全书'}
    # return render(request, 'home.html', {'info_dict': info_dict})

    # 示例六:模板中的逻辑操作

    # 示例七:获取当前用户
    # return render(request, 'home.html')

    # 示例八: 获取当前网址
    return render(request, 'home.html')



