from django.shortcuts import render

# view for index page
def index(request):
    return render(request, 'index.html')
# view for about page
def about(request):
    return  render(request, 'about.html')