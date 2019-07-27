from django.test import TestCase
from app.models import *
import hashlib
import time
from django.db import transaction
from django.db import IntegrityError
# Create your tests here.

class PersonageModelTest(TestCase):
    """
    Test personage model:
        - setting default values
        - special logic in updating fileds
    """
    def test_personage_create(self):
        # test create personage without pars
        Personage.objects.create()
        self.assertEqual(Personage.objects.count(),1)
        self.assertIsNotNone(Personage.objects.get(id=1).create_dt)
        self.assertEqual(Personage.objects.get(id=1).enemy_killed_cnt,0)
        # test create personage with name
        Personage.objects.create(name='Vasya')
        self.assertEqual(Personage.objects.get(id=2).name,'Vasya')
        # test create personage with name and clan
        test_clan = Clan.objects.create(name='Investigators')
        Personage.objects.create(name='Petya', clan=test_clan)
        self.assertEqual(Personage.objects.get(id=3).clan.id, test_clan.id)

    def test_personage_update(self):
        # test set password
        test_psw = 'Password'
        test_personage = Personage.objects.create(name='Petya')
        test_personage.set_psw(test_psw)
        self.assertIsNotNone(test_personage.psw)
        self.assertNotEqual(test_personage.psw, test_psw)
        self.assertEqual(test_personage.psw, hashlib.sha224(test_psw.encode()).hexdigest())
        self.assertEqual(test_personage.enemy_killed_cnt,0)
        # test kill enemy
        test_personage.kill_enemy()
        self.assertEqual(test_personage.enemy_killed_cnt,1)

    def test_change_clan_value(self):
        # Can change only from None to clan (join to clan) or clan to None (withdraw from clan)
        test_personage = Personage.objects.create()
        test_clan_1 = Clan.objects.create(name="Test Clan 1")
        test_clan_2 = Clan.objects.create(name="Test Clan 2")
        test_personage.clan = test_clan_1
        test_personage.save()
        self.assertEqual(Personage.objects.get(id=test_personage.id).clan.name, "Test Clan 1")
        test_personage.clan = test_clan_2
        test_personage.save()
        self.assertNotEqual(Personage.objects.get(id=test_personage.id).clan.name, "Test Clan 2")
        test_personage.clan = None
        test_personage.save()
        self.assertIsNone(Personage.objects.get(id=test_personage.id).clan)
        test_personage.clan = test_clan_2
        test_personage.save()
        self.assertEqual(Personage.objects.get(id=test_personage.id).clan.name, "Test Clan 2")

class InventoryModelTest(TestCase):
    """
    Test inventory model:
        - setting default values
        - special logic in updating fileds
    """
    def test_inventory_create(self):
        # test inventory to be created only with personage and item. 
        # Noone can break these relations
        test_personage = Personage.objects.create()
        test_item = Item.objects.create()
        error = False
        try:
            with transaction.atomic():
                Inventory.objects.create()
        except IntegrityError:
            error = True
        self.assertTrue(error)
        error = False
        try:
            with transaction.atomic():
                Inventory.objects.create(personage=test_personage)
        except IntegrityError:
            error = True
        self.assertTrue(error)
        error = False
        try:
            with transaction.atomic():
                Inventory.objects.create(item=test_item)
        except IntegrityError:
            error = True
        self.assertTrue(error)
        error = False
        try:
            with transaction.atomic():
                Inventory.objects.create(personage=test_personage, item=test_item)
        except IntegrityError:
            error = True
        self.assertFalse(error)
        # check default values
        self.assertEqual(Inventory.objects.get(id=1).item_location, 'backpack')
        self.assertEqual(Inventory.objects.get(id=1).item_uses_count, 0)

    def test_inventory_update(self):
        test_inventory = Inventory.objects.create(personage=Personage.objects.create(), item=Item.objects.create())
        test_inventory.use_item()
        self.assertEqual(test_inventory.item_uses_count, 1)

    def test_change_inventory_values(self):
        # Can not change personage and item
        test_personage_1 = Personage.objects.create(name="Test Personage 1")
        test_personage_2 = Personage.objects.create(name="Test Personage 2")
        test_item_1 = Item.objects.create(name="Test Item 1")
        test_item_2 = Item.objects.create(name="Test Item 2")
        test_inventory = Inventory.objects.create(personage=test_personage_1, item=test_item_1)
        test_inventory.personage = test_personage_2
        test_inventory.item_uses_count = 3
        test_inventory.item_location = 'storage'
        test_inventory.save()
        self.assertEqual(Inventory.objects.get(id=test_inventory.id).personage.name, "Test Personage 1")
        self.assertEqual(Inventory.objects.get(id=test_inventory.id).item_uses_count, 3)
        self.assertEqual(Inventory.objects.get(id=test_inventory.id).item_location, 'storage')
        test_inventory.item = test_item_2
        test_inventory.item_uses_count = 5
        test_inventory.item_location = 'belt'
        test_inventory.save()
        self.assertEqual(Inventory.objects.get(id=test_inventory.id).item.name, "Test Item 1")
        self.assertEqual(Inventory.objects.get(id=test_inventory.id).item_uses_count, 5)
        self.assertEqual(Inventory.objects.get(id=test_inventory.id).item_location, 'belt')
        test_inventory.personage = test_personage_2
        test_inventory.item = test_item_2
        test_inventory.save()
        self.assertEqual(Inventory.objects.get(id=test_inventory.id).personage.name, "Test Personage 1")
        self.assertEqual(Inventory.objects.get(id=test_inventory.id).item.name, "Test Item 1")

class PersonageLocationModelTest(TestCase):
    """
    Test personage location model:
        - setting default values
    """
    def test_location_create(self):
        # test inventory to be created only with personage and item. 
        # Noone can break these relations
        test_personage = Personage.objects.create()
        test_location = Location.objects.create()
        error = False
        try:
            with transaction.atomic():
                PersonageLocation.objects.create()
        except IntegrityError:
            error = True
        self.assertTrue(error)
        error = False
        try:
            with transaction.atomic():
                PersonageLocation.objects.create(personage=test_personage)
        except IntegrityError:
            error = True
        self.assertTrue(error)
        error = False
        try:
            with transaction.atomic():
                PersonageLocation.objects.create(location=test_location)
        except IntegrityError:
            error = True
        self.assertTrue(error)
        error = False
        try:
            with transaction.atomic():
                PersonageLocation.objects.create(personage=test_personage, location=test_location)
        except IntegrityError:
            error = True
        self.assertFalse(error)
        # check default values
        self.assertIsNotNone(PersonageLocation.objects.get(id=1).last_visited_dt)

    def test_change_location_values(self):
        # Can not change personage and location
        test_personage_1 = Personage.objects.create(name="Test Personage 1")
        test_personage_2 = Personage.objects.create(name="Test Personage 2")
        test_location_1 = Location.objects.create(name="Test Location 1")
        test_location_2 = Location.objects.create(name="Test Location 2")
        test_personagelocation = PersonageLocation.objects.create(personage=test_personage_1, location=test_location_1)
        test_personagelocation.personage = test_personage_2
        test_personagelocation.save()
        self.assertEqual(PersonageLocation.objects.get(id=test_personagelocation.id).personage.name, "Test Personage 1")
        test_personagelocation.location = test_location_2
        test_personagelocation.save()
        self.assertEqual(PersonageLocation.objects.get(id=test_personagelocation.id).location.name, "Test Location 1")
        test_personagelocation.personage = test_personage_2
        test_personagelocation.location = test_location_2
        test_personagelocation.save()
        self.assertEqual(PersonageLocation.objects.get(id=test_personagelocation.id).personage.name, "Test Personage 1")
        self.assertEqual(PersonageLocation.objects.get(id=test_personagelocation.id).location.name, "Test Location 1")
