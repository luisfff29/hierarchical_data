from django.shortcuts import render, reverse
from animals.models import Animals, Usuario
from django.views.generic import FormView, View
from django.contrib.auth import login, logout, authenticate
from animals.forms import AnimalsForm, LoginForm, SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


# Create your views here.
class Index(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html', {
            'animals': Animals.objects.filter(
                author=get_object_or_404(
                    Usuario, username=request.user.username
                ))})


class Create_Animal(LoginRequiredMixin, View):
    def get(self, request):
        form = AnimalsForm()
        form.fields['parent'].queryset = form.fields['parent'].queryset.filter(
            author=Usuario.objects.get(username=request.user.username))
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AnimalsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Animals.objects.create(
                name=data['name'],
                parent=data['parent'],
                author=get_object_or_404(
                    Usuario, username=self.request.user.username
                ))
            return HttpResponseRedirect(reverse('home'))


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
            else:
                return render(request, 'login.html', {'form': LoginForm()})


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
