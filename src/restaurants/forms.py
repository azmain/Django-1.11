from django.forms import ModelForm
from .models import Restaurant
from django import forms
#from .validators import validate_category

class RestaurantCreateForm(ModelForm):
	#it can be done in model itslef
	#category = forms.CharField(required=False,validators=[validate_category])
	class Meta:
		model = Restaurant
		fields = [
			'name',
			'location',
			'category',
			'my_date',
			'slug'
		]
	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == 'Hello':
			raise forms.ValidationError('Not a valid name')

		return name