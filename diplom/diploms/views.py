from django.shortcuts import render



def index(request):
    return render(request, 'diploms/home.html')
def about_us(request):
    return render(request, 'diploms/about_us.html')
def katalog(request):
    return render(request, 'diploms/katalog.html')
def events(request):
    return render(request, 'diploms/events.html')

