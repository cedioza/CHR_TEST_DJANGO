# Generated by Django 4.2.2 on 2023-06-21 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JudicialSearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valor',
            name='idItemlista',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
