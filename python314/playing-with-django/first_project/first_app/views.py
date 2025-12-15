from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User


# Create your views here.
def companies(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records": webpages_list}

    return render(request, "first_app/companies.html", context=date_dict)

def index(request):
    return render(request, "first_app/index.html")

def help_me(request):
    helpDict = {'help_insert':"HELP PAGE"}
    return render(request, "help/help.html", context=helpDict)

def users(request):
    users_list = User.objects.order_by('first_name')
    users_dict ={ "users": users_list}
    return render(request, "first_app/users.html", context=users_dict)




