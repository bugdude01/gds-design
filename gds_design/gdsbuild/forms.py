from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Fieldset, HTML
from crispy_forms.bootstrap import FieldWithButtons, StrictButton, InlineField, InlineRadios

import datetime

#  Keep
class TestForm(forms.Form):

    STATUSES = (
        ("A", "All transactions"),
        ("C", "Complete only"),
        ("I", "Incomplete only"),
        ("W", "Whatever else"),
    )
    
    years = [x for x in range(1900,2019)]
    months = [(i, datetime.date(2008, i, 1).strftime('%B')) for i in range(1,13)]
    days = [x+1 for x in range(31)]

    YEARS = [x for x in range(1900,2019)]


    check_box = forms.TypedChoiceField(
        label = "Check Box", 
        choices = ((0, "this"),(1, "and this"),(2, "some of this too?"),(3, "Oh go on then, hy not?")), 
        widget = forms.CheckboxSelectMultiple,
        initial = '0',
        required = True,
    )
    # Done

    date_Picker = forms.IntegerField(
        min_value = 1,
        widget=forms.NumberInput
    )
    # Done

    radios_side = forms.ChoiceField(
        label = "Inline Radio Buttons",
        choices = ((1, "Either"), (0, "Or")),
        widget = forms.RadioSelect,
        initial = '1',
        required = False,
    )
    # Done

    radio_buttons = forms.ChoiceField(
        label = "Radio Buttons",
        choices = ((0, "Please"),(1, "Make"), (2, "Your"), (3, "Choice")),
        # coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    # Done

    dropdown = forms.ChoiceField(
        widget=forms.Select,
        label = "Select",
        choices=STATUSES, 
        initial="A"
    )
    # Done

    less_text = forms.CharField(
        label = "A litle bit of text",
        widget = forms.TextInput,
    )
    # Done

    more_text = forms.CharField(
        label = "Quite a bit more text",
        widget = forms.Textarea,
    )
    # Done


    helper = FormHelper()
    helper.form_method = "GET"
    helper.csrf_token = False
    helper.layout = Layout(
        Field("check_box"),
        Field("date_Picker"),
        InlineRadios("radios_side"),
        Field("radio_buttons"),
        Field("dropdown"),
        Field("less_text"),
        Field("more_text")
    )


#  Keep
class LoginForm(forms.Form):

    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput,
    )

    password = forms.CharField(
        label = "Password",
        widget =forms.PasswordInput,
        required = True,
    )

    helper = FormHelper()
    helper.form_method = "GET"
    helper.csrf_token = False
    helper.layout = Layout(
        Field("username"),
        Field("password")
        
    )


# Keep
class SignupsForm(forms.Form):
    STATUSES = (
        ("S", "Sole Trader"),
        ("L", "Limited Company"),
        ("C", "Corporation"),
    )

    company_name = forms.CharField(
        label = "Company Name",
        widget = forms.TextInput,
    )

    address_line_1 = forms.CharField(
        label = "Address",
        widget = forms.TextInput,
    )

    address_line_2 = forms.CharField(
        label = "",
        widget = forms.TextInput,
    )

    town = forms.CharField(
        label = "Town or City",
        widget = forms.TextInput,
    )

    postcode = forms.CharField(
        label = "Postcode",
        widget = forms.TextInput,
    )

    bus_type = forms.ChoiceField(
        widget = forms.Select,
        label = "Type of business",
        choices=STATUSES, 
        initial="S"
    )

    date_Picker = forms.IntegerField(
        min_value = 1,
        label = "Business Start Date",
        widget=forms.NumberInput
    )

    email = forms.CharField(
        label = "Email Address",
        widget = forms.EmailInput,
        required = True,
    )

    password = forms.CharField(
        label = "Password",
        widget =forms.PasswordInput,
        required = True,
    )

    password_conf = forms.CharField(
        label = "Confirm Password",
        widget = forms.PasswordInput,
        required = True,
    )

    helper = FormHelper()
    helper.form_method = "POST"
    helper.csrf_token = True
    helper.layout = Layout(
        Field("company_name"),
        Field("address_line_1"),
        Field("address_line_2"),
        Field("town"),
        Field("postcode"),
        Field("bus_type"),
        Field("date_Picker"),
        Field("email"),
        Field("password"),
        Field("password_conf"),
    )


# Keep
class SimpleSignup(forms.Form):

    # error_css_class = 'govuk-input govuk-input--error'
    # required_css_class = 'required'

    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput,
    )

    password1 = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput,
        required = True,
    )

    password2 = forms.CharField(
        label = "Re-Ener Password",
        widget = forms.PasswordInput,
        required = True,
    )

    helper = FormHelper()
    helper.form_method = "POST"
    helper.csrf_token = True
    helper.layout = Layout(
        Field("username"),
        Field("password1"),
        Field("password2"),
    )



years = [x for x in range(1900,2019)]
months = [(i, datetime.date(2008, i, 1).strftime('%B')) for i in range(1,13)]
days = [x+1 for x in range(31)]


#  Keep
class TransactionFilterForm(forms.Form):
    STATUSES = (
        ("A", "All transactions"),
        ("C", "Complete only"),
        ("I", "Incomplete only"),
        ("W", "Whatever else"),
    )
    
    YEARS = [x for x in range(1900,2019)]

    status = forms.ChoiceField(choices=STATUSES, initial="A")
    from_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    to_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    more_info = forms.CharField(widget=forms.Textarea(), label="Your Text in here please", required=True)
    helper = FormHelper()
    helper.form_method = "GET"
    helper.csrf_token = False
    helper.layout = Layout(

        Field("status"),
        Field("from_date"),
        Field("to_date"),
        Field("more_info")
    )


# Next task
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()