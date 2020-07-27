# Generated by Django 3.0.8 on 2020-07-27 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrimonio',
            name='acquisition_document_number',
            field=models.CharField(max_length=10, null=True, verbose_name='Nota Fiscal de aquisição'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='acquisition_date',
            field=models.DateField(null=True, verbose_name='Data de aquisição'),
        ),
        migrations.AlterField(
            model_name='patrimonio',
            name='value',
            field=models.DecimalField(decimal_places=2, help_text='Valor de aquisição', max_digits=8, null=True, verbose_name='Valor'),
        ),
    ]
