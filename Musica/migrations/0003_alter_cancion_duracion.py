# Generated by Django 4.0.5 on 2022-07-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musica', '0002_alter_cancion_duracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='duracion',
            field=models.IntegerField(max_length=5),
        ),
    ]
