from django.shortcuts import render
from animals.models import Animals
from django.views.generic import FormView
from animals.forms import AnimalsForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {'animals': Animals.objects.all()})


class Create_Animal(FormView):
    template_name = 'form.html'
    form_class = AnimalsForm
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data
        Animals.objects.create(name=data['name'], parent=data['parent'])
        return super().form_valid(form)
