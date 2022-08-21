from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product, Report, Remake, Reason
from django.core.paginator import Paginator
from .forms import ReportForm, ProductForm
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

# def count(request):
#     month_value = Report.

def base(request):

    num_reports_of_day = Report.objects.filter(date_field__contains=datetime.today().date()).count()
    num_reports_of_month = Report.objects.filter(user=request.user).filter(date_field__contains=datetime.now().month).aggregate(Sum('number_of_new_plates'))
    context = {
        'num_reports_of_day': num_reports_of_day,
        'num_reports_of_month':num_reports_of_month,
    }

    return render(request, 'base.html', context=context)

def index(request):

    num_reports = Report.objects.all().count()
    num_reports_of_day = Report.objects.filter(date_field__contains=datetime.today().date()).count()
    # num_reports_of_month = Report.objects.filter(user=request.user).filter(date_field__contains=datetime.now().month).aggregate(Sum('number_of_new_plates'))
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_reports': num_reports,
        'num_visits': num_visits, 
        'num_reports_of_day': num_reports_of_day,
        # 'num_reports_of_month':num_reports_of_month,               
    }

    return render(request, 'index.html', context=context)

@login_required
def report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()        
            return HttpResponseRedirect('/ataskaitos/report/')
    else:
        form = ReportForm() 
    num_reports_of_day = Report.objects.filter(date_field__contains=datetime.today().date()).count()
    num_reports_of_month = Report.objects.filter(user=request.user).filter(date_field__contains=datetime.now().month).aggregate(Sum('number_of_new_plates'))
    paginator = Paginator(Report.objects.filter(user=request.user).order_by('-date_field'), 20)
    page_number = request.GET.get('page')
    paged_reports = paginator.get_page(page_number)
    context = {
        'report': paged_reports,
        'form': form,
        'num_reports_of_day': num_reports_of_day, 
        'num_reports_of_month':num_reports_of_month,     
    }
    
    return render(request, 'report.html', context=context)


# @login_required
# def master(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.save()          
#             return HttpResponseRedirect('/ataskaitos/master/')
#     else:
#         form = ProductForm() 
#     context = {
#         'form': form,

#     }

#     return render(request, 'master.html',context=context)

def master(request):

    form=ProductForm
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request, 'master.html', context)


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')





