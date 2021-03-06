from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import (get_object_or_404, 
                              render,
                              redirect,
                              HttpResponseRedirect) 

from .forms import PublicContactsForm, UpdateAccountForm, RegisterForm, UpdateForm
from .models import Account, PublicContacts
from project.models import Service
from django.views.generic.edit import UpdateView
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

# Generic view para criar um novo utilizador
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('needsbox:index')

    # Se o utilizador for criado com sucesso envio um email de agradecimento pelo registo
    def form_valid(self, form):
        name=form.cleaned_data.get('name')
        msg_plain = render_to_string('email-register.html', {'name': name})
        msg_html = render_to_string('email-register.html', {'name': name})
        message = "Olá {name}, nem vindo ao NeedsBox!".format(
            name=form.cleaned_data.get('name'),)
        send_mail(
            subject="Obrigado pelo registo!",
            message=msg_plain,
            from_email='system@scutelniciuc.xyz',
            recipient_list=[form.cleaned_data.get('email')],
            html_message=msg_html,
        )
        return super().form_valid(form)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


class AccountDetailView(generic.DetailView):
    model = Account
    slug_field = "username"

def profile(request, username):
    context = {}

    try:
        user = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return render(request, 'pages/404-error.html', context=context)

    if user.get_type() != 'PRO':
        return render(request, 'pages/404-error.html', context=context)

    services = Service.objects.filter(user=user)

    try:
        public_contacts = PublicContacts.objects.get(user=user)
    except PublicContacts.DoesNotExist:
        public_contacts = 0
    review_count = 0
    service_count = 0

    for service in services:
        service_count += 1
        review_count += service.get_reviews_count()

    context = {
        'user': user,
        'services': services,
        'review_count': review_count,
        'service_count': service_count,
        'contacts': public_contacts,
    }

    return render(request, 'profile.html', context=context)


def user_delete_view(request, username):
    obj = get_object_or_404(Account, username=username)
    if request.method == "POST":
        obj.delete()
        return redirect('needsbox:index')
    context = {
        "object": obj
    }
    return render(request, 'user_delete.html', context)

# update view for user
def update_view(request, username): 
    context ={} 
    obj = get_object_or_404(Account, username = username) 
    form = UpdateAccountForm(request.POST or None, request.FILES or None, instance = obj) 
    context["form"] = form 
    if form.is_valid(): 
        form.save() 
        return render(request, "profile-edit.html", context) 
    return render(request, "profile-edit.html", context) 

def update_info_view(request, username): 
    context ={}
    user = get_object_or_404(Account, username = username) 
    #obj = get_object_or_404(PublicContacts, user = user) 
    try:
        obj = PublicContacts.objects.get(user=user)
    except PublicContacts.DoesNotExist:
        form = PublicContactsForm(request.POST or None, user=user)
        if form.is_valid():
            form.user = user
            form.save()
            return render(request, "profile-edit-info.html", context)
        context = {"form": form}
        return render(request, "profile-edit-info.html", context)
    form = PublicContactsForm(request.POST or None, request.FILES or None, instance = obj) 
    context["form"] = form 
    if form.is_valid(): 
        form.save() 
        return render(request, "profile-edit-info.html", context) 
    return render(request, "profile-edit-info.html", context)


