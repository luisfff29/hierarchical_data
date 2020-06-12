from django.shortcuts import render
from animals.models import Animals


# Create your views here.
def index(request):
    return render(request, 'index.html', {'animals': Animals.objects.all()})
