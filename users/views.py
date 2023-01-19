from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from common.views import Title_Mixin
from products.models import Basket

from .forms import User_Login_Form, User_Profile_Form, User_Register_Form
from .models import Email_Verification, User


class Email_Verification_View(Title_Mixin, TemplateView):
    title = 'Store - Подтверждение email адресса'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = self.kwargs['code']
        user = User.objects.get(email=self.kwargs['email'])
        email_verifications = Email_Verification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(Email_Verification_View, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))


class User_Login_View(Title_Mixin, LoginView):
    template_name = 'users/login.html'
    form_class = User_Login_Form
    title = 'Store - Авторизация'


class User_Registration_View(Title_Mixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = User_Register_Form
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрировались'
    title = 'Store - Регистрация'


class User_Profile_View(Title_Mixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = User_Profile_Form
    title = 'Store - Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    # def get_context_data(self, **kwargs):
    #     context = super(User_Profile_View, self).get_context_data()
    #     context['baskets'] = Basket.objects.filter(user=self.object)
    #     return context

# def register(request):
#     if request.method == 'POST':
#         form = User_Register_Form(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегестрировались')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = User_Register_Form
#     context = {'form': form}
#     return render(request, 'users/register.html', context)


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = User_Profile_Form(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = User_Profile_Form(instance=request.user)
#
#     context = {
#         'title': 'Профиль',
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user)
#     }
#     return render(request, 'users/profile.html', context)

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))

# def login(request):
#     if request.method == 'POST':
#         form = User_Login_Form(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = User_Login_Form()
#     context = {'form': form}
#     return render(request, 'users/login.html', context)
