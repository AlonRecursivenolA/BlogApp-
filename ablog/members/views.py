from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from theblog.models import Profile
from .forms import UserRegisterForm, ProfilePageForm

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "register/create_profile_page.html"
    #fields = ['bio', 'profile_pic', 'facebook_url', 'instgram_url', 'twitter_url']

    def form_valid(self, form):
        form.instance.user = self.request.user #We do not change it in the form! so this method is required to add value in the DB!
        return super().form_valid(form)
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'register/user_profile_edit.html'
    fields = ['bio', 'profile_pic', 'facebook_url', 'instagram_url', 'twitter_url']
    success_url = reverse_lazy('ListView')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'register/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        user = Profile.objects.all()

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        context['page_user'] = page_user
        return context


class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('login')


class UpdateFormView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('ListView')

    def get_object(self):
        return self.request.user

#
# class ChangePasswordView(PasswordChangeView):
#     form_class = PasswordChangeForm
#     template_name = 'registration/change_password.html/'
#     success_url = reverse_lazy('registration/password_changed')
