from django.shortcuts import render

# Create your views here.

def login(req):
    if req.method == "POST":
        if 1:
            # return redirect("/yuan_back/")
            name = "yuanhao"
            return render(req, "my backend.html", locals())
    return render(req, "login.html", locals())

def yuan_back(req):
    name = "苑昊"
    return render(req, "my backend.html", locals())