from django.shortcuts import render, redirect

# Create your views here.

def login(req):
    if req.method == "POST":
        if 1:  # 指代登陆成功
            return redirect("/home/")
            # name = "Vito"
            # return render(req, "home.html", locals())
    return render(req, "login_views.html", locals())


def home(req):
    name = "Vito"
    return render(req, "home.html", {"name": name})
