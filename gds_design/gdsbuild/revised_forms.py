from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Fieldset, HTML
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from allauth.account.forms import SignupForm

import datetime

class ExampleForm(forms.Form):

    STATUSES = (
        ("A", "All transactions"),
        ("C", "Complete only"),
        ("I", "Incomplete only"),
    )
    
    YEARS = [x for x in range(1900,2019)]

    status = forms.ChoiceField(
        choices=STATUSES, 
        initial="A"
    )

    from_date = forms.DateField(
        widget=forms.SelectDateWidget(years=YEARS)
    )

    to_date = forms.DateField(
        widget=forms.SelectDateWidget(years=YEARS)
    )

    more_info = forms.CharField(
        widget=forms.Textarea(), 
        label="Your Text in here please", required=True
    )


    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    Checkbox = forms.TypedChoiceField(
        label = "Pick one", 
        choices = ((0, "either"),(1, "or")), 
        widget = forms.CheckboxInput,
        initial = '0',
        required = True,
    )

    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    file_upload = forms.FileInput(
        label = "Upload a File",
        widget = forms.FileInput,
    )

    helper = FormHelper()
    helper.form_method = "GET"
    helper.csrf_token = False
    helper.layout = Layout()