from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse

def year_archive(request):
    # ...
    year = [2006,]
    # ...
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))

    #return render(request, "dat.html", {"year": year})