from django.shortcuts import render
from .models import poi

def index(request):
    #pois = poi.objects.all()
    return render(request, "index.html", {"pois":pois})

class poi:
    def __init__(self, name, relative_skill, priority, category, progress):
        self.name = name
        self.relative_skill = relative_skill
        self.priority = priority
        self.category = category
        self.progress = progress

pois = {
    poi("Job", "programming testing", 5, "money and self-expression", 50),
    poi("Movie making", "treveling", 3, "usefull hobbie", 35),
    poi("Sport", "poledancing", 4, "health", 25),
    poi("DL", "trevelling", 4, "car", 100)
}
