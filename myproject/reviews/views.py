from django.http import HttpResponse
from django.shortcuts import render

def index (request):
     # 1.1
     return render(request, "base.html")


def ind (request):
     # 1.2
     search = request.GET.get("search");
     return render(request, "base.html", {"search": search});
