from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from matplotlib.style import context
from .models import Product, Report, Remake, Reason
# from django.views import generic
from django.core.paginator import Paginator
from .forms import ReportForm


def index(request):

    num_reports = Report.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_reports': num_reports,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

def report(request):
    # submitted = False
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, 'report.html', submitted=True)

            return HttpResponseRedirect('/ataskaitos/report/')
    else:
        form = ReportForm() 
    #     if 'submitted' in request.GET:
    #         submitted = True   
    paginator = Paginator(Report.objects.filter(user=request.user).order_by('-date_field'), 10)
    page_number = request.GET.get('page')
    paged_reports = paginator.get_page(page_number)
    context = {
        'report': paged_reports,
        'form': form,
        # 'submitted': submitted, 
    }
    
    return render(request, 'report.html', context=context)




