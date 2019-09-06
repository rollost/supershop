from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello from supershop index page</h1>")
