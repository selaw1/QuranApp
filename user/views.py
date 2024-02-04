from django.contrib import messages
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView

from user.forms import RegistrationForm
from user.models import UserBase

from .token import account_activation_token


class UserCreateView(CreateView):
    model = UserBase
    form_class = RegistrationForm
    template_name = 'user/registration/registration.html'
    success_url = reverse_lazy('user:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(self.request)

        # Email Activation Setup
        current_site = get_current_site(self.request)
        subject = 'Activate Your Account'
        message = render_to_string('user/registration/account_activation_email.html', {
            'user':user,
            'domain':current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        user.email_user(subject=subject, message=message)

        # Success message
        messages.add_message(
            self.request,
            messages.INFO,
            'Check Your Email For Account Activation Link'
        )
        return super().form_valid(form)

def account_activation(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)

    except():
        pass

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'user/registration/activation_invalid.html')
