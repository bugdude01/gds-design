from django import forms, template

register = template.Library()

@register.filter
def is_datefield(field):
	return isinstance(field.field.widget, forms.SelectDateWidget)

@register.filter
def is_select(field):
	return isinstance(field.field.widget, forms.Select)

@register.filter
def is_email(field):
	return isinstance(field.field.widget, forms.EmailInput)

@register.filter
def is_password(field):
	return isinstance(field.field.widget, forms.PasswordInput)

# | | | Smaller Text Box Field | | |
# V V V                        V V V
@register.filter
def is_textinput(field):
	return isinstance(field.field.widget, forms.TextInput)

# | | | Larger Text Box Field | | |
# V V V                       V V V
@register.filter
def is_textarea(field):
	return isinstance(field.field.widget, forms.Textarea)

@register.filter
def is_number(field):
	return isinstance(field.field.widget, forms.NumberInput)