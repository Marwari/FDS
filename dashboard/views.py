from django.shortcuts import render

# view for index page
def index(request):
    return render(request, 'index.html')
