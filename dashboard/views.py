import numpy as np
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template

from dashboard.notebook.creditcard import credit_model
from dashboard.notebook.bank import bank_model
from dashboard.notebook.mobile_data import mobile_model
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

# bank fraud page
def bank(request):
    return render(request, 'bank.html')
# creditcard fraud page
@login_required(login_url='/login/')
def creditcard(request):
    return render(request, 'creditcard.html')
# mobile transaction
@login_required(login_url='/login/')
def mobilefraud(request):
    return render(request, 'mobile.html')

#banking services
@login_required(login_url='/login/')
def bankresult(request):
    # get the data and print prediction
    age = request.POST.get("age")
    job = request.POST.get("job")
    marital = request.POST.get("marital")
    education = request.POST.get("education")
    balance = request.POST.get("balance")
    housing = request.POST.get("housing")
    loan = request.POST.get("loan")
    duration = int(request.POST.get("duration"))
    poutcome = int(request.POST.get("poutcome"))
    bank_data = np.array([age,job,marital,education,balance,housing,loan,duration,poutcome])
    # print(bank_data)
    clf = bank_model()
    c = clf.predict([bank_data])
    print(c)
    if c == [1]:
        # print("Not fraud")
        response = 'Not Fraud'
    else:
        # print("Fraud")
        response = 'Fraud'
    return render(request, 'bank/result.html', {"result": response})

# credit card services
@login_required(login_url='/login/')
def creditresult(request):
    if request.method == "POST":
        # get the data and print
        limit_balance = request.POST.get("limit_balance")
        sex = request.POST.get("sex")
        print(sex)
        if(sex=="Male"):
            new_sex = 1
        else:
            new_sex = 2
        print(new_sex)
        education = request.POST.get("education")
        print(education)
        if (education=="Graduate"):
            new_education = 1
        elif (education=="University"):
            new_education = 2
        elif (education == "High School"):
            new_education = 3
        elif (education == "Others"):
            new_education = 4
        else:
            new_education = 5 or 6
        print(new_education)

        marriage = request.POST.get("marriage")
        age = request.POST.get("age")
        pay_1 = int(request.POST.get("pay_1"))
        pay_2 = int(request.POST.get("pay_2"))
        pay_3 = int(request.POST.get("pay_3"))
        pay_4 = int(request.POST.get("pay_4"))
        pay_5 = int(request.POST.get("pay_5"))
        pay_6 = int(request.POST.get("pay_6"))
        Bill_Amt_1 = int(request.POST.get("Bill_Amt_1"))
        Bill_Amt_2 = int(request.POST.get("Bill_Amt_2"))
        Bill_Amt_3 = int(request.POST.get("Bill_Amt_3"))
        Bill_Amt_4 = int(request.POST.get("Bill_Amt_4"))
        Bill_Amt_5 = int(request.POST.get("Bill_Amt_5"))
        Bill_Amt_6 = int(request.POST.get("Bill_Amt_6"))
        Pay_Amt_1 = int(request.POST.get("Pay_Amt_1"))
        Pay_Amt_2 = int(request.POST.get("Pay_Amt_2"))
        Pay_Amt_3 = int(request.POST.get("Pay_Amt_3"))
        Pay_Amt_4 = int(request.POST.get("Pay_Amt_4"))
        Pay_Amt_5 = int(request.POST.get("Pay_Amt_5"))
        Pay_Amt_6 = int(request.POST.get("Pay_Amt_6"))

        credit_data = np.array([limit_balance, new_sex, new_education, marriage, age, pay_1, pay_2, pay_3, pay_4, pay_5, pay_6, Bill_Amt_1, Bill_Amt_2, Bill_Amt_3, Bill_Amt_4, Bill_Amt_5, Bill_Amt_6, Pay_Amt_1, Pay_Amt_2, Pay_Amt_3, Pay_Amt_4, Pay_Amt_5, Pay_Amt_6])
        print(credit_data)
        clf = credit_model()
        c = clf.predict([credit_data])
        print(c)
        if c == [0]:
            response = 'Not a Fraud'
        else:
            response = 'fraud'
        # print(c)
        return render(request, 'creditcard/result.html', {"result": response})
    else:
        return redirect('/creditcard',request)

# mobile fraud services
@login_required(login_url='/login/')
def mobileresult(request):
    # get the data and print
    type = request.POST.get("type")
    amount = request.POST.get("amount")
    nameOrig = request.POST.get("nameOrig")
    oldbalanceOrg = request.POST.get("oldbalanceOrg")
    newbalanceOrig = request.POST.get("newbalanceOrig")
    nameDest = request.POST.get("nameDest")
    oldbalanceDest = request.POST.get("oldbalanceDest")
    newbalanceDest = request.POST.get("newbalanceDest")
    # isFraud = int(request.POST.get("isFraud")))
    isFlaggedFraud = 1
    mobile_data = np.array([type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest,oldbalanceDest, newbalanceDest, isFlaggedFraud])
    # print(bank_data)
    clf = mobile_model()
    c = clf.predict([mobile_data])
    print(c)
    if c == [0]:
        # print("Not fraud")
        response = 'Not Fraud'
    else:
        # print("Fraud")
        response = 'Fraud'
    return render(request, 'mobile/result.html', {"result": response})