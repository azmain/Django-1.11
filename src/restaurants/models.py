from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name	= models.CharField(max_length=120)
	location = models.CharField(max_length=120,null=True,blank=True)
	category = models.CharField(max_length=120,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated   = models.DateTimeField(auto_now=True)
	my_date   = models.DateField(auto_now=False,auto_now_add=False)
	slug      = models.SlugField(null=True,blank=True)
	def __str__(self):
		return self.name

	@property 
	def title(self):
		return self.name


from django.db.models.signals import pre_save, post_save
from restaurants.utils import unique_slug_generator

#pre and post save are mostly same but pre is better to use
def rl_pre_save_receiver(sender,instance,*args,**kwargs):
	# print('saving...')
	# print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver,sender=Restaurant)