from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# def home(request):
# 	return HttpResponse("hello")
# Function based views
# def home(request):
# 	context = {
# 		'context': 'good'
# 	}
# 	return render(request,"home.html",context)

# def about(request):
# 	context = {
# 		'context': 'good'
# 	}
# 	return render(request,"about.html",context)

# def contact(request):
# 	context = {
# 		'context': 'good'
# 	}
# 	return render(request,"contact.html",context)


# view
# class ContactView(View):
# 	def get(self,request,*args,**kwargs):
# 		context = {}
# 		return render(request,"contact.html",context)

# TemplateView
class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self,*args,**kwargs):
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		context = {
			"char": "good"
		}
		return context

class AboutView(TemplateView):
	template_name = "about.html"

class ContactView(TemplateView):
	template_name = "contact.html"


# Restaurant App
from .models import Restaurant
# function based view
def restaurant_view(request):
	template_name = 'restaurants/restaurant.html'
	queryset = Restaurant.objects.all()
	context = {
		"list": queryset
	}
	return render(request,template_name,context)


#class based view
class RestaurantView(LoginRequiredMixin,ListView):
	template_name = 'restaurants/restaurant.html'
	login_url = '/login'
	def get_queryset(self):
		return Restaurant.objects.filter(owner=self.request.user)

from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

class RestaurantDetailView(LoginRequiredMixin,DetailView):
	template_name = 'restaurants/restaurant_detail.html'
	login_url = '/login'
	def get_queryset(self):
		return Restaurant.objects.filter(owner=self.request.user)

	# For understanding what context returns
	# def get_context_data(self,*args,**kwargs):
	# 	print(self.kwargs)
	# 	context = super(RestaurantDetailView,self).get_context_data(*args,**kwargs)
	# 	print(context)
	# 	return context

	#looking by id
	# def get_object(self,*args,**kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(Restaurant,id=rest_id) #pk=rest_id
	# 	return obj

from django.views.generic import CreateView
from django import forms
from .forms import RestaurantCreateForm


class RestaurantCreateView(LoginRequiredMixin,CreateView):
	form_class = RestaurantCreateForm
	login_url = '/login'
	template_name = 'create.html'
	#success_url = '/restaurant/'

	def form_valid(self,form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(RestaurantCreateView,self).form_valid(form)

	def get_context_data(self,*args,**kwargs):
		context = super(RestaurantCreateView,self).get_context_data(*args,**kwargs)
		context['title'] = 'Restaurants'
		return context


class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
	form_class = RestaurantCreateForm
	login_url = '/login'
	template_name = 'restaurants/detail-update.html'
	#success_url = '/restaurant/'

	def get_context_data(self,*args,**kwargs):
		context = super(RestaurantUpdateView,self).get_context_data(*args,**kwargs)
		name = self.get_object().name
		context['title'] = f'Update Restaurant: {name}'
		return context

	def get_queryset(self):
		return Restaurant.objects.filter(owner=self.request.user)
