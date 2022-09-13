from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem
def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_katalog,
        'name': 'Dimitri Prima Nugraha',
        'id': '2106750396',
    }
    return render(request, "katalog.html", context)
