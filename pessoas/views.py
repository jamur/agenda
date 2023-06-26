import re
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
# Create your views here.

def home(request):
    return render(request, "pessoas/home.html")

def about(request):
    return render(request, "pessoas/about.html")

def contact(request):
    return render(request, "pessoas/contact.html")

def home_antigo(request):
    return HttpResponse("Hello, Pessoas!")

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        "pessoas/hello_there.html",
        {
            'name': name,
            'date': datetime.now()
        }
    )

def hello_there_antigo(request, name):
    print(request.build_absolute_uri()) #optional
    now = datetime.now()
    formatted_now = now.strftime("%A, %d de %B de %Y e são %X")

    # Filter the name argument to letters only using regular expressions. URL arguments.
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Oi, " + clean_name + "! Tudo bem? Hoje é " + formatted_now
    return HttpResponse(content)
