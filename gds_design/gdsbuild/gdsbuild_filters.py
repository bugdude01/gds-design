from django import forms, template

register = template.Library()

@register.filter
def is_datefield(field):
	return isinstance(field.field.widget, forms.SelectDateWidget)