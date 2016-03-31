from django.shortcuts import render
from django.shortcuts import redirect
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(email=request.POST['email'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return redirect('/', new_user='yes')
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    return render(request, 'register.html', args)


def account(request):
    context = {}
    context['user'] = request.user
    return render(request, 'index.html', context)