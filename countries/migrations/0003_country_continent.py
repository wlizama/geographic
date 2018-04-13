# Generated by Django 2.0.3 on 2018-04-13 02:37

from django.db import migrations, models
import django.db.models.deletion


def ceate_continent(apps, schema_editor):
    Continent = apps.get_model("continents", "Continent")

    Continent.objects.create(name="asia", color="#B01D1D", translate="asia")
    Continent.objects.create(name="america", color="#58B249", translate="america")
    Continent.objects.create(name="antartida", color="#BB2974", translate="antartida")
    Continent.objects.create(name="europa", color="#079959", translate="europa")
    Continent.objects.create(name="áfrica", color="##2200D2", translate="áfrica")
    Continent.objects.create(name="oceania", color="#303030", translate="oceania")

class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0001_initial'),
        ('countries', '0002_auto_20180410_0227'),
    ]

    operations = [
    migrations.RunPython(ceate_continent),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='continents.Continent'),
            preserve_default=False,
        ),
    ]
