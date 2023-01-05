from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def racer_list(request):   # ReadAll Racers Method
    racers = models.Racer.objects.all()
    context = {'racers': racers}
    return render(request, 'racer_list.html', context)

def racer_detail(request, pk): # Read Racer Method 
    racer = get_object_or_404(models.Racer, pk=pk)
    context = {'racer': racer}
    return render(request, 'racer_detail.html', context)