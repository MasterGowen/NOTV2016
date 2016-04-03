from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.shortcuts import resolve_url, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import UpdateView
from django.utils.translation import ugettext as _

from .forms import RegistrationForm

from .models import NOTVUser

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



def account(request):
    user = request.user

    context = {'user': user}
    context['user'] = request.user
    return render(request, 'account.html', context)


@csrf_protect
def password_change(request,
                    template_name='password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    extra_context=None):

    post_change_redirect = resolve_url('/user/password/done/')
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # Updating the password logs out all other sessions for the user
            # except the current one.
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'title': _('Password change'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


class NOTVUserUpdate(UpdateView):
    model = NOTVUser
    fields = ['avatar', 'first_name', 'last_name', 'department', 'position', 'tel', 'status']

    def get_object(self):
        return get_object_or_404(NOTVUser, pk=self.request.session['_auth_user_id'])

    def get_context_data(self, **kwargs):

        context = super(NOTVUserUpdate, self).get_context_data(**kwargs)
        context['user'] = get_object_or_404(NOTVUser, pk=self.request.session['_auth_user_id'])

        return context