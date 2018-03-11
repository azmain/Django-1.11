"""django111 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from restaurants.views import (
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
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^menus/', include('menus.urls', namespace='menus')),
    url(r'^restaurant/', include('restaurants.urls', namespace='restaurant')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^reset/$', PasswordResetView.as_view(), name='password_reset'),
    #url(r'^restaurant/$', RestaurantView.as_view(), name='restaurant'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
]
