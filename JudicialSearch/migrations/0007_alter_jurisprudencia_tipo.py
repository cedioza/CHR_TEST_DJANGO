# Generated by Django 4.0.10 on 2023-06-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JudicialSearch', '0006_alter_jurisprudencia_caratula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencia',
            name='tipo',
            field=models.CharField(max_length=50),
        ),
    ]