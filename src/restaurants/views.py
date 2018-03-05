from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

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

from .models import Restaurant
def restaurant_view(request):
	template_name = 'restaurants/restaurant.html'
	queryset = Restaurant.objects.all()
	context = {
		"list": queryset
	}
	return render(request,template_name,context)