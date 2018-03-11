from django.conf import settings
from django.db import models

from restaurants.models import Restaurant
from django.urls import reverse
# Create your models here.
class Item(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	restaurant = models.ForeignKey(Restaurant)

	#main data
	name = models.CharField(max_length=120)
	contents = models.TextField(help_text='Separated by comma')
	excludes = models.TextField(blank=True,null=True,help_text='Separated by comma')
	public  = models.BooleanField(default=True)
	updated = models.TimeField(auto_now=True)
	timestamp = models.TimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('menus:detail', kwargs={'pk': self.id})


	class Meta:
		ordering = ['-updated','-timestamp']

	def get_contents(self):
		return self.contents.split(',')

	def get_excludes(self):
		return self.excludes.split(',')

