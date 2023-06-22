# Generated by Django 4.0.10 on 2023-06-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JudicialSearch', '0009_alter_jurisprudencia_caratula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencia',
            name='caratula',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='jurisprudencia',
            name='descriptores',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='jurisprudencia',
            name='linkSentencia',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='jurisprudencia',
            name='nombreProyecto',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='jurisprudencia',
            name='relacionada',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='jurisprudencia',
            name='urlSentencia',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='valor',
            name='item',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='valor',
            name='parametro',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='valor',
            name='valor',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]
