from django.db import models


class Patrimonio(models.Model):
    title = models.CharField(verbose_name='Título', max_length=100, blank=False, null=False)
    value = models.DecimalField(verbose_name='Valor', help_text='Valor de aquisição', max_digits=8,
                                decimal_places=2, null=True, blank=True)
    acquisition_date = models.DateField(verbose_name='Data de aquisição', null=True, blank=True)
    description = models.TextField(verbose_name='descrição', blank=True)
    acquisition_document_number = models.CharField(verbose_name='Nota Fiscal de aquisição', max_length=10,
                                                   null=True, blank=True)

    def __str__(self):
        return self.title

