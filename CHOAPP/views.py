from django.http import HttpResponse

def index(request):
    return HttpResponse("CHOAPP says hey there partner!")