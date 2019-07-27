"""stalker_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import (
    ClanList, ClanCreate, ClanUpdate, ClanDelete,
    PersonageList, PersonageCreate, PersonageUpdate, PersonageDelete,
    ItemList, ItemCreate, ItemUpdate, ItemDelete,
    InventoryList, InventoryCreate, InventoryUpdate, InventoryDelete,
    LocationList, LocationCreate, LocationUpdate, LocationDelete,
    PersonageLocationList, PersonageLocationCreate, PersonageLocationUpdate, PersonageLocationDelete,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="main.html"), name='main'),
    path('clans/', ClanList.as_view(),  name='clans'),
    path('clan_create/', ClanCreate.as_view(), name='clan-create'),
    path('clan_update/<int:pk>/', ClanUpdate.as_view(), name='clan-update'),
    path('clan_delete/<int:pk>/', ClanDelete.as_view(), name='clan-delete'),
    path('personages/', PersonageList.as_view(),  name='personages'),
    path('personage_create/', PersonageCreate.as_view(), name='personage-create'),
    path('personage_update/<int:pk>/', PersonageUpdate.as_view(), name='personage-update'),
    path('personage_delete/<int:pk>/', PersonageDelete.as_view(), name='personage-delete'),
    path('items/', ItemList.as_view(),  name='items'),
    path('item_create/', ItemCreate.as_view(), name='item-create'),
    path('item_update/<int:pk>/', ItemUpdate.as_view(), name='item-update'),
    path('item_delete/<int:pk>/', ItemDelete.as_view(), name='item-delete'),
    path('inventories/', InventoryList.as_view(),  name='inventories'),
    path('inventory_create/', InventoryCreate.as_view(), name='inventory-create'),
    path('inventory_update/<int:pk>/', InventoryUpdate.as_view(), name='inventory-update'),
    path('inventory_delete/<int:pk>/', InventoryDelete.as_view(), name='inventory-delete'),
    path('locations/', LocationList.as_view(),  name='locations'),
    path('location_create/', LocationCreate.as_view(), name='location-create'),
    path('location_update/<int:pk>/', LocationUpdate.as_view(), name='location-update'),
    path('location_delete/<int:pk>/', LocationDelete.as_view(), name='location-delete'),
    path('personagelocations/', PersonageLocationList.as_view(),  name='personagelocations'),
    path('personagelocation_create/', PersonageLocationCreate.as_view(), name='personagelocation-create'),
    path('personagelocation_update/<int:pk>/', PersonageLocationUpdate.as_view(), name='personagelocation-update'),
    path('personagelocation_delete/<int:pk>/', PersonageLocationDelete.as_view(), name='personagelocation-delete'),
]

