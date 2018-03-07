from django.core.exceptions import ValidationError


CATEGORY = [
	'All',
	'Indian',
	'Chinese',
	'Mexican',
	'Bengali'
]



def validate_category(value):
	cat = value.capitalize()
	if value not in CATEGORY and cat not in CATEGORY:
		raise ValidationError(
            f'{value} not a valid category'
        )