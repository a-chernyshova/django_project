from django.shortcuts import render
from .models import poi

def index(request):
    #pois = poi.objects.all()
    return render(request, "index.html", {"pois":pois})

class poi:
    def __init__(self, name, relative_skill, priority, category, progress, img_url):
        self.name = name
        self.relative_skill = relative_skill
        self.priority = priority
        self.category = category
        self.progress = progress
        self.img_url = img_url

pois = {
#    poi("Job", "programming testing", 5, "money and self-expression", 50, 'http://i2.cdn.turner.com/money/dam/assets/150123172021-i-love-my-job-mug-1024x576.jpg'),
#    poi("Movie making", "treveling", 3, "usefull hobbie", 35, 'http://headrush.in/outbound/wp-content/uploads/2015/04/Movie-making4.jpg'),
#    poi("Sport", "poledancing", 4, "health", 25, 'https://i.ytimg.com/vi/rCRP-5om_3Y/maxresdefault.jpg'),
#    poi("DL", "trevelling", 4, "car", 100, 'http://kratomblast.com/wp-content/uploads/2015/10/Kratom-and-Driving.jpg')
}
