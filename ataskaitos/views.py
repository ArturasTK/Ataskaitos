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

    # return HttpResponse("Hello World!")
