from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Vagabond Engineer Home</h1>')
