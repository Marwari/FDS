from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .forms import ContactForm, UserLoginForm


# view for index page
def index(request):
    return render(request, 'index.html')
# view for about page
def about(request):
    return  render(request, 'about.html')

### contact view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }

            content = template.render(context)
            email = EmailMessage(
                "New contact form submission",
                content,
                "FDS" + '',
                ['b200jst@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('/success')

    return render(request, 'contact.html', {
        'form': form_class,
    })

# success page
def success(request):
    return render(request, 'success.html')

# login page
def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, 'login.html',{"form":form})

# logout view
@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return render(request, "index.html")

# service view
@login_required(login_url='/login/')
def services(request):
    return render(request, 'services.html')