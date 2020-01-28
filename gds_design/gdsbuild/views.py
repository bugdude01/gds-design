from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import TestForm, TransactionFilterForm, SignupsForm, LoginForm, SimpleSignup
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return HttpResponse("Hello World")

def base(request):
    return render(request, "gds_base.html")

def help(request):
    return render(request, "gds_help.html")

def home(request):
    return render(request, "gds_home.html")

def split(request):
    return render(request, "containers/gds_2_plus_1_splitcontainer.html")

def split_home(request):
    return render(request, "gds_split_home.html")


#  | | | | | FORMS | | | | |
#  V V V V V       V V V V V

# Keep
def form_tester(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    
    return render(
        request, 'forms/accounts/form_tester.html', {
        'form': form, 
        } 
        )

# keep
def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupsForm()

    
    return render(
        request, 'forms/accounts/signup.html', {
        'form': form, 
        } 
        )

# Keep
def simple_signup(request):

    form = SimpleSignup()
    if request.method == 'POST':

        if request.POST['password1'] == request.POST['password2']:
            form = SimpleSignup(request.POST)
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'forms/accounts/simple_signup.html', {
                    'error': 'Username has already been taken',
                    'form': form,
                })
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'forms/accounts/simple_signup.html', {
                    'error': 'Passwords must match',
                    'form': form,
                })

    return render(
        request, 'forms/accounts/simple_signup.html', {
        'form': form,
        }
        )

# keep
def login(request):

    form = LoginForm()
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            form = LoginForm(request.POST)
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'forms/accounts/login.html', {
                'form': form,
                'error': 'username or password are incorrect!'
                })

    else:
        form = LoginForm()

    
    return render(
        request, 'forms/accounts/login.html', {
        'form': form, 
        }
        )

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

# | | | | File Upload | | | |
# V V V V             V V V V

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/successful/url')
        else:
            form = UploadFileForm()
        return  render(request, 'upload.html', {'form': form})




    # | | | | | Error Page Views | | | | |
    # V V V V V                  V V V V V

def view_404(request, *args, **kwargs):
    response = render_to_response("errors/404.html")
    response.status_code = 404
    return response

def view_500(request, *args, **kwargs):
    response = render_to_response("errors/500.html")
    response.status_code = 500
    return response

def view_503(request, *args, **kwargs):
    response = render_to_response("errors/503.html")
    response.status_code = 503
    return response

    # | | | | | Accounts Views | | | | |
    # V V V V V                V V V V V


