from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from pousadas.forms import PousadaForm

from pousadas.models import Pousada

class PousadaList(SuccessMessageMixin, ListView):
    model = Pousada
    queryset = Pousada.objects.all()

class PousadaCreate(SuccessMessageMixin, CreateView):
    model = Pousada
    form_class = PousadaForm
    success_message = "Pousada cadastrada com sucesso! Clique em detalhes para ver mais informações!"
    success_url = reverse_lazy('pousadas:list')
    
class PousadaUpdate(SuccessMessageMixin, UpdateView):
    model = Pousada
    form_class = PousadaForm
    success_message = "Pousada editada com sucesso! Clique em detalhes para ver mais informações!"
    success_url = reverse_lazy('pousadas:list')

class PousadaDetail(DetailView):
    queryset = Pousada.objects.all()

class PousadaDelete(SuccessMessageMixin, DeleteView):
    queryset = Pousada.objects.all()
    success_url = reverse_lazy('pousadas:list')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "A Pousada foi apagada com sucesso!"