from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.


def loginUser(request):
    errors = False
    if(request.POST):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('/cameras/')
            return response
        else:
           errors = True
            # Return an 'invalid login' error message.
    template = loader.get_template('accounts/login.html')
    context = { 'errors' : errors}
    return HttpResponse(template.render(context, request))

def logoutUser(request):
    print(request)
    logout(request)
    response = redirect('/')
    return response