from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dect = {
        "insert_me":'Hello from the app veiews.py',
        "my_name":'caeser'
    }
    return render(request, "first_app/index.html", context=my_dect)

def hello(request):
    return HttpResponse("<h1>Hello, Hello, Hello</h1>")

def help(request):
    helpDict = {'help_insert':"HELP PAGE"}
    return render(request, "help/help.html", context=helpDict)




