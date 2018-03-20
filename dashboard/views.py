import numpy as np
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template

from dashboard.notebook.creditcard import credit_model
from dashboard.notebook.bank import bank_model
from dashboard.notebook.mobile_data import mobile_model

from dashboard.notebook.graphs import result

from dashboard.notebook.mobile_analytics import mobile_result

from dashboard.notebook.creditcard_analytics import creditcard_result
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
@login_required(login_url='/login/')
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
    print(job)
    if (job == "Unemployed"):
        new_job = 1
    elif (job == "Management"):
        new_job = 2
    elif (job == "Services"):
        new_job = 3
    elif (job == "Blue-Collar"):
        new_job = 4
    elif (job == "Entrepreneur"):
        new_job = 5
    elif (job == "Admin"):
        new_job = 6
    elif (job == "Unknown"):
        new_job = 7
    elif (job == "Self-employed"):
        new_job = 8
    elif (job == "Student"):
        new_job = 9
    elif (job == "House maid"):
        new_job = 10
    elif (job == "Technician"):
        new_job = 11
    elif (job == "Retired"):
        new_job = 12
    print(new_job)
    marital = request.POST.get("marital")
    if (marital == "Single"):
        new_marital = 1
    elif (marital == "Divorced"):
        new_marital = 2
    elif (marital == "Married"):
        new_marital = 3
    print(new_marital)
    education = request.POST.get("education")
    if (education == "Unknown"):
        new_education = 1
    elif (education == "Primary"):
        new_education = 2
    elif (education == "Secondary"):
        new_education = 3
    elif (education == "Graduate"):
        new_education = 4
    print(new_education)
    balance = request.POST.get("balance")
    housing = request.POST.get("housing")
    if (housing == "Yes"):
        new_housing = 1
    elif (housing == "No"):
        new_housing = 2
    print(new_housing)
    loan = request.POST.get("loan")
    if (loan == "Yes"):
        new_loan = 1
    elif (loan == "No"):
        new_loan = 2
    print(new_loan)
    duration = int(request.POST.get("duration"))
    campaign = int(request.POST.get('campaign'))
    pdays = int(request.POST.get('pdays'))
    previous = int(request.POST.get('previous'))
    poutcome = (request.POST.get("poutcome"))
    if (poutcome == "Unknown"):
        new_poutcome = 3
    elif (poutcome == "Failure"):
        new_poutcome = 1
    elif (poutcome == "Successs"):
        new_poutcome = 4
    elif (poutcome == "Failure"):
        new_poutcome = 2
    print(new_poutcome)
    bank_data = np.array([age,new_job,new_marital,new_education,balance,new_housing,new_loan,duration,campaign,pdays,previous,new_poutcome])
    clf = bank_model()
    c = clf.predict([bank_data])
    print(c)
    if c == [1]:
        # print("Not fraud")
        response = 'Not Fraud'
    else:
        # print("Fraud")
        response = 'Fraud'


    accuracy = 0.8962983425414365
    return render(request, 'bank/result.html', {"result": response, 'accuracy':accuracy})

# analytics
# def analysis(request):
#     return render(request, 'analysis.html', {'accuracy': accuracy})

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
        if (education == "Primary"):
            new_education = 1
        elif (education == "Secondary"):
            new_education = 2
        elif (education == "Graduate"):
            new_education = 3
        print(new_education)
        marriage = request.POST.get("marriage")
        if (marriage == "Single"):
            new_marriage = 1
        elif (marriage == "Married"):
            new_marriage = 2
        elif (education == "Divorced"):
            new_marriage = 3
        print(new_marriage)
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
        credit_data = np.array([limit_balance, new_sex, new_education, new_marriage, age, pay_1, pay_2, pay_3, pay_4, pay_5, pay_6, Bill_Amt_1, Bill_Amt_2, Bill_Amt_3, Bill_Amt_4, Bill_Amt_5, Bill_Amt_6, Pay_Amt_1, Pay_Amt_2, Pay_Amt_3, Pay_Amt_4, Pay_Amt_5, Pay_Amt_6])
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
    step = request.POST.get("step")
    type = request.POST.get("type")
    if (type == "Payment"):
        new_type = 1
    elif (type == "Transfer"):
        new_type = 4
    elif (type == "Cash-out"):
        new_type = 5
    elif (type == "Debit"):
        new_type = 2
    print(new_type)
    amount = request.POST.get("amount")
    nameOrig = request.POST.get("nameOrig")
    oldbalanceOrg = request.POST.get("oldbalanceOrg")
    newbalanceOrig = request.POST.get("newbalanceOrig")
    nameDest = request.POST.get("nameDest")
    oldbalanceDest = request.POST.get("oldbalanceDest")
    newbalanceDest = request.POST.get("newbalanceDest")
    # isFraud = int(request.POST.get("isFraud")))
    isFlaggedFraud = 1
    mobile_data = np.array([step, new_type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest,oldbalanceDest, newbalanceDest, isFlaggedFraud])
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

# analytics page
def analytics(request):
    return render(request, 'analytics.html', {'analytics':result, "mobile_analytics": mobile_result, "creditcard_analytics": creditcard_result})