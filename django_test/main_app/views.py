from django.shortcuts import render
from .models import poi
#from django.http import HttpResponse

def index(request):
    #context = { "name": Job question, "num_st": 7,}
    #return HttpResponse("<h1>Wake up, Neo!</h1>")
    points_of_interest = poi.objects.all()
    return render(request, "index.html", {"points_of_interest":points_of_interest})

class point_of_interest:
    def __init__(self, name, relative_skill, priority, category, progress):
        self.name = name
        self.relative_skill = relative_skill
        self.priority = priority
        self.category = category
        self.progress = progress

points_of_interest = {
    point_of_interest("job", "programming testing", 5, "money and self-expression", 50),
    point_of_interest("movie making", "treveling", 3, "usefull hobbie", 35),
    point_of_interest("sport", "poledancing", 4, "health", 25),
    point_of_interest("DL", "trevelling", 4, "car", 100)
}