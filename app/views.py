from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from app.forms import PersonageForm
from django.views.generic.edit import FormView

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from app.models import (Clan, Personage, Item, Inventory, Location, PersonageLocation)

class ClanCreate(CreateView):
    model = Clan
    fields = '__all__'
    success_url = reverse_lazy('clans')

class ClanUpdate(UpdateView):
    model = Clan
    fields = '__all__'
    success_url = reverse_lazy('clans')

class ClanDelete(DeleteView):
    model = Clan
    fields = '__all__'
    success_url = reverse_lazy('clans')

class ClanList(ListView):
    model = Clan

class PersonageCreate(FormView):
    model = Personage
    form_class = PersonageForm
    template_name = 'app/personage_form.html'
    success_url = reverse_lazy('personages')
    def form_valid(self, form):
        personage = form.save(commit=False)
        personage.set_psw(personage.psw)
        return super().form_valid(form)

class PersonageUpdate(UpdateView):
    model = Personage
    fields = ['name', 'clan', 'enemy_killed_cnt', 'last_visit_dt']
    success_url = reverse_lazy('personages')

class PersonageDelete(DeleteView):
    model = Personage
    success_url = reverse_lazy('personages')

class PersonageList(ListView):
    model = Personage

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('items')

class ItemUpdate(UpdateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('items')

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('items')

class ItemList(ListView):
    model = Item

class InventoryCreate(CreateView):
    model = Inventory
    fields = '__all__'
    success_url = reverse_lazy('inventories')

class InventoryUpdate(UpdateView):
    model = Inventory
    fields = '__all__'
    success_url = reverse_lazy('inventories')

class InventoryDelete(DeleteView):
    model = Inventory
    success_url = reverse_lazy('inventories')

class InventoryList(ListView):
    model = Inventory

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'
    success_url = reverse_lazy('locations')

class LocationUpdate(UpdateView):
    model = Location
    fields = '__all__'
    success_url = reverse_lazy('locations')

class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy('locations')

class LocationList(ListView):
    model = Location

class PersonageLocationCreate(CreateView):
    model = PersonageLocation
    fields = '__all__'
    success_url = reverse_lazy('personagelocations')

class PersonageLocationUpdate(UpdateView):
    model = PersonageLocation
    fields = '__all__'
    success_url = reverse_lazy('personagelocations')

class PersonageLocationDelete(DeleteView):
    model = PersonageLocation
    success_url = reverse_lazy('personagelocations')

class PersonageLocationList(ListView):
    model = PersonageLocation
