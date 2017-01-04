from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Don't worry, learn math part</h1>")
