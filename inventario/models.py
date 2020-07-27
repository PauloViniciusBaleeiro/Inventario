from django.db import models


class Tipo(models.Model):
    TIPOS_DE_HD = (
        (1, 'HDD'),
        (2, 'SSD'),
    )
    description = models.CharField(verbose_name='Descrição', max_length=50,
                                   help_text='Deixar os detalhes em branco, caso não seja um computador')
    hd_size = models.IntegerField(verbose_name='Capacidade de armazenamento HD(GB)', blank=True,
                                  null=True)
    hd_type = models.CharField(verbose_name='Tipo de HD', choices=TIPOS_DE_HD, max_length=1,
                               blank=True, null=True)
    memory_size = models.IntegerField(verbose_name='Tamanho da memória(GB)', blank=True, null=True)
    processor = models.CharField(verbose_name='Processador', max_length=20, blank=True, null=True)
    os = models.CharField(verbose_name='Sistema operacional', max_length=30, blank=True, null=True)
    obs = models.TextField(verbose_name='Observação', blank=True, null=True)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.description + ' ' + self.os + '/' + self.processor + self.memory_size + \
               'gb/HD' + self.hd_type


class Patrimonio(models.Model):
    title = models.CharField(verbose_name='Título', max_length=100, blank=False, null=False)
    value = models.DecimalField(verbose_name='Valor', help_text='Valor de aquisição', max_digits=8,
                                decimal_places=2, null=True, blank=True)
    acquisition_date = models.DateField(verbose_name='Data de aquisição', null=True, blank=True)
    description = models.TextField(verbose_name='Descrição', blank=True)
    acquisition_document_number = models.CharField(verbose_name='Nota Fiscal de aquisição', max_length=10,
                                                   null=True, blank=True)
    serial_number = models.CharField(verbose_name='Número de série', max_length=50, null=True, blank=True)
    term = models.CharField(verbose_name='Termo de responsabilidade', max_length=200, null=True, blank=True)
    date_term = models.DateField(verbose_name='Data de registro do termo', null=True, blank=True)
    term_expires_at = models.DateField(verbose_name='Termo expira em ', null=True, blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, blank=True, null=True)
    brand = models.CharField(verbose_name='Marca', max_length=100, blank=True, null=True)
    model = models.CharField(verbose_name='Modelo', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Patrimônio'
        verbose_name_plural = 'Patrimônios'

    def __str__(self):
        return self.title

