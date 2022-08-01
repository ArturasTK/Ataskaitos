from django.shortcuts import render
from django.http import HttpResponse
# from matplotlib.style import context
from .models import Product, Report, Remake, Reason

def index(request):

    num_reports = Report.objects.all().count()
    context = {
        'num_reports': num_reports,
    }

    return render(request, 'index.html', context=context)

def report(request):
    
    report = Report.objects.filter(user=request.user).order_by('-date_field')
    context = {
        'report': report
    }
    print(report)
    return render(request, 'report.html', context=context)
    # return HttpResponse("Hello World!")
