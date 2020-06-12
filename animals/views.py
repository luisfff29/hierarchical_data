from django.shortcuts import render, reverse
from animals.models import Animals, Usuario
from django.views.generic import FormView, View
from django.contrib.auth import login, logout, authenticate
from animals.forms import AnimalsForm, LoginForm, SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Index(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html', {'animals': Animals.objects.all()})


class Create_Animal(LoginRequiredMixin, FormView):
    template_name = 'form.html'
    form_class = AnimalsForm
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data
        Animals.objects.create(name=data['name'], parent=data['parent'])
        return super().form_valid(form)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/login/'

    def form_valid(self, form):
        data = form.cleaned_data
        Usuario.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            is_staff=False,
            is_superuser=False
        )
        return super().form_valid(form)
