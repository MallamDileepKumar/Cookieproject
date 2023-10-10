from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def add(request):
    x = int(request.GET['t1'])
    y = int(request.GET['t2'])
    z = x+y
    res = HttpResponse(f"""<center><i><h1 style='color:red'>Data submitted successfully!</center></i><h1>""")

    res.set_cookie('z',z,max_age=100)
    return res
def display(request):
    if 'z' in request.COOKIES:
        sum = str(request.COOKIES['z'])
        return HttpResponse(f"""<center><i><h1 style='color:red'>The sum of the two number are : {sum} </center></i><h1>""")
    else:
        return HttpResponse(f"""<center><i><h1 style='color:red'>Plz enter the two values</center></i><h1>""")
