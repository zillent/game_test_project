from django.db import models
import hashlib
from datetime import datetime
# Create your models here.

"""
TODO:
1. - таблица с записями о персонажах: имя, клан, дата создания, дата последнего входа в игру, пароль, счетчик убитых противников
Personage + Clan
2. - таблица с записями об инвентаре персонажа: ид персонажа, ид предмета, кол-во использований предмета, расположение предмета (рюкзак, пояс, хранилище)
Perosnage + Item + Inventory
3. - таблица с перемещениями персонажа: ид персонажа, ид локации, дата последнего визита
Personage + Location + PersonageLocation
4. - все гриды должны иметь кросс-ссылки на связанные сущности и возможностью изменения любого параметра, кроме связей.
???
"""

class Clan(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True, verbose_name='Наименование клана')
    def __str__(self):
        return self.name

"""
"""

class PersonageManager(models.Manager):
    pass

class Personage(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True, verbose_name='Имя персонажа')
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE, default=None, blank=True, null=True, verbose_name='Клан')
    create_dt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_visit_dt = models.DateTimeField(default=None, blank=True, null=True, verbose_name='Дата последнего посещения')
    psw = models.CharField(max_length=50, verbose_name='Пароль')
    enemy_killed_cnt = models.IntegerField(default=0, verbose_name='Счетчик убитых врагов')
    objects = PersonageManager()
    def set_psw(self, psw):
        ''' Hash and set passwword '''
        if psw is not None:
            self.psw = hashlib.sha224(psw.encode()).hexdigest()
            self.save()
    def kill_enemy(self):
        self.enemy_killed_cnt+=1
        self.save()
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        # По идее лучше эти проверки делать в триггере базы данных
        old_personage_clan = None
        if self._state.adding:
            self.last_visit_dt=datetime.now()
        else:
            old_personage_clan = Personage.objects.get(id=self.id).clan
        if old_personage_clan is not None:
            if self.clan is not None and self.clan.id != old_personage_clan.id:
                self.clan = old_personage_clan
        return super().save(*args, **kwargs)

class Item(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True, verbose_name='Название предмета') 
    def __str__(self):
        return self.name

class Inventory(models.Model):
    personage = models.ForeignKey(Personage, on_delete=models.CASCADE, verbose_name='Персонаж')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Предмет')
    item_uses_count = models.IntegerField(default=0, verbose_name='Количество использований предмета')
    ITEM_LOCATIONS = (
        ('backpack', 'Рюкзак'),
        ('belt', 'Пояс'),
        ('storage', 'Хранилище'),
    )
    item_location = models.CharField(max_length=100, choices=ITEM_LOCATIONS, default='backpack', verbose_name='Расположение предмета')
    def use_item(self):
        self.item_uses_count+=1
        self.save()
    def __str__(self):
        return self.item.name+'->'+self.personage.name+' ('+self.item_location+')'
    def save(self, *args, **kwargs):
        # По идее лучше эти проверки делать в триггере базы данных
        if not self._state.adding:
            old_inventory = Inventory.objects.get(id=self.id)
            self.personage = old_inventory.personage
            self.item = old_inventory.item
        return super().save(*args, **kwargs)

class Location(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True, verbose_name='Наименование локации') 
    def __str__(self):
        return self.name

class AutoDateTimeField(models.DateTimeField):
    # for future
    pass

class PersonageLocation(models.Model):
    personage = models.ForeignKey(Personage, on_delete=models.CASCADE, verbose_name='Персонаж')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')
    last_visited_dt = models.DateTimeField(default=None, blank=True, null=True, verbose_name='Дата последнего посещения')
    def __str__(self):
        return self.personage.name+'->'+self.location.name
    def save(self, *args, **kwargs):
        # По идее лучше эти проверки делать в триггере базы данных
        if self._state.adding:
            self.last_visited_dt=datetime.now()
        else:
            old_perconagelocation = PersonageLocation.objects.get(id=self.id)
            self.personage = old_perconagelocation.personage
            self.location = old_perconagelocation.location
        return super().save(*args, **kwargs)
