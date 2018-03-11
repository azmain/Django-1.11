from django.conf.urls import url

from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView
)

urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='list'),
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'^update/$', ItemUpdateView.as_view(), name='update'),
    # url(r'^restaurant/(?P<slug>\w+)$', RestaurantView.as_view()),
    url(r'^(?P<pk>[\w-]+)/$', ItemDetailView.as_view(), name='detail')
]
