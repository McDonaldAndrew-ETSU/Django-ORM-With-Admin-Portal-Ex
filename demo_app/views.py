from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def racer_list(request):   # ReadAll Racers Method
    racers = models.Racer.objects.all()
    context = {'racers': racers}
    return render(request, 'racer_list.html', context)

def racer_detail(request, pk): # Read Racer Method 
    racer = get_object_or_404(models.Racer, pk=pk)
    context = {'racer': racer}
    return render(request, 'racer_detail.html', context)


class RacerCreateView(generic.CreateView):
    model = models.Racer
    template_name = 'racer_create_update_form_generic.html'
    fields = ['name', 'skill']


class RacerListView(generic.ListView):
    queryset = models.Racer.objects.all()
    template_name = 'racer_list_generic.html'
    context_object_name = 'racers2'

class RacerDetailView(generic.DetailView):
    model = models.Racer
    template_name = 'racer_detail_generic.html'
    context_object_name = 'racer2'


class RacerUpdateView(generic.UpdateView):
    model = models.Racer
    template_name = 'racer_create_update_form_generic.html'
    fields = ['name', 'skill']

class RacerDeleteView(generic.DeleteView):
    model = models.Racer
    template_name = 'racer_delete_generic.html'
    context_object_name = 'racer2'
    success_url = reverse_lazy('racer_list2')

