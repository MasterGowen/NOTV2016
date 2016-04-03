from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

import logging


logger = logging.getLogger(__name__)


@csrf_protect
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(email=request.POST['email'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect('/')
        else:
            logger.info('Invalid form')
    else:
        form = RegistrationForm()
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    return render(request, 'register.html', args)


def index(request):
    context = {}
    context['user'] = request.user
    return render(request, 'index.html', context)


@login_required()
def account(request):
    context = {}
    context['user'] = request.user
    return render(request, 'passport.html', context)