from django.conf.urls import url

from .views import (
    HomeView,
    AboutView,
    ContactView,
    restaurant_view,
    RestaurantView,
    RestaurantDetailView,
    RestaurantCreateView
)
from django.contrib.auth.views import LoginView,PasswordResetView

urlpatterns = [
    url(r'^$', RestaurantView.as_view(), name='list'),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    # url(r'^restaurant/(?P<slug>\w+)$', RestaurantView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail')
]
