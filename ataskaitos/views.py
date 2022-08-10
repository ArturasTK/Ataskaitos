from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product, Report, Remake, Reason
from django.core.paginator import Paginator
from .forms import ReportForm
from datetime import datetime

# def count(request):
#     month_value = Report.

def base(request):

    num_reports_of_day = Report.objects.filter(date_field__contains=datetime.today().date()).count()
    context = {
        'num_reports_of_day': num_reports_of_day,
    }

    return render(request, 'base.html', context=context)

def index(request):

    num_reports = Report.objects.all().count()
    num_reports_of_day = Report.objects.filter(date_field__contains=datetime.today().date()).count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_reports': num_reports,
        'num_visits': num_visits, 
        'num_reports_of_day': num_reports_of_day,       
    }

    return render(request, 'index.html', context=context)

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
   
    paginator = Paginator(Report.objects.filter(user=request.user).order_by('-date_field'), 20)
    page_number = request.GET.get('page')
    paged_reports = paginator.get_page(page_number)
    context = {
        'report': paged_reports,
        'form': form,      
    }
    
    return render(request, 'report.html', context=context)




