from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList
# Create your views here.
def show_watchlist_index(request):
    watchlist = MyWatchList.objects.all()
    count_watched = 0
    count_unwatched = 0
    res = False
    
    for item in watchlist:
        if item.watched:
            count_watched += 1
        else:
            count_unwatched += 1
    if count_watched >= count_unwatched:
        res = True
    
    context = {
        'is_watched_more': res,
    }
    return render(request, 'watchlist_bonus.html', context)

def show_watchlist(request):
    watchlist = MyWatchList.objects.all()
    context = {
        'watchlist': watchlist,
        'nama' : 'Dimitri Prima Nugraha',
        'id' : '2106750396'
    }
    return render(request, 'watchlist.html', context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
def show_html(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('html', data), content_type='application/html')

