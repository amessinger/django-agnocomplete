"""
Agnostic Autocomplete URLS
"""
from django.conf.urls import patterns, url
from .views import AgnocompleteView, CatalogView

urlpatterns = [
    url(
        r'^(?P<klass>[-_\w]+)/$',
        AgnocompleteView.as_view(),
        name='agnocomplete'),
    url(r'^$', CatalogView.as_view(), name='catalog'),
]

urlpatterns = patterns('', *urlpatterns)
