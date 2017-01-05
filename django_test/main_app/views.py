from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    name = "blablabla"
    num = 1000
    context = {
        "name": name,
        "num": num}
    #return HttpResponse("<h1>Wake up, Neo!</h1>")
    return render(request, "index.html", context)