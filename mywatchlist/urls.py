
from django.urls import path
from mywatchlist.views import show_watchlist_index, show_watchlist, show_xml, show_json, show_html

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist_index, name='index'),
    path('xml/', show_xml, name='xml'),
    path('json/', show_json, name='json'),
    path('html/', show_watchlist, name='html'),
]
