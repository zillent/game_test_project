# Generated by Django 2.2.2 on 2019-06-15 17:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190614_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Наименование клана'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='clan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Clan', verbose_name='Клан'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='enemy_killed_cnt',
            field=models.IntegerField(default=0, verbose_name='Счетчик убитых врагов'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='last_visit_dt',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now, verbose_name='Дата последнего посещения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personage',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Имя персонажа'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='psw',
            field=models.CharField(max_length=50, verbose_name='Пароль'),
        ),
    ]
