from django.shortcuts import render

# Create your views here.
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView
	)
from .models import Item
from .forms import ItemForm
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

class ItemListView(LoginRequiredMixin,ListView):
	login_url = '/login'
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemDetailView(LoginRequiredMixin,DetailView):
	login_url = '/login'
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)



class ItemCreateView(LoginRequiredMixin,CreateView):
	form_class = ItemForm
	login_url = '/login'
	template_name = 'create.html'
	def form_valid(self,form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(ItemCreateView,self).form_valid(form)

	def get_form_kwargs(self):
		kwargs = super(ItemCreateView,self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self,*args,**kwargs):
		context = super(ItemCreateView,self).get_context_data(*args,**kwargs)
		context['title'] = 'Menu Item'
		return context

class ItemUpdateView(LoginRequiredMixin,UpdateView):
	form_class = ItemForm
	login_url = '/login'
	template_name = 'menus/detail-update.html'
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_form_kwargs(self):
		kwargs = super(ItemUpdateView,self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def get_context_data(self,*args,**kwargs):
		context = super(ItemUpdateView,self).get_context_data(*args,**kwargs)
		name = self.get_object().name
		context['title'] = f'Update Item: {name}'
		return context