from django.db import models
from cpf_field.models import CPFField


class Proposal(models.Model):
    name = models.CharField(
        verbose_name='Nome Completo', max_length=255, null=False, blank=False
    )
    cpf = CPFField('cpf', null=False, blank=False)
    address = models.CharField(
        verbose_name='Endereço', max_length=255, null=False, blank=False
    )
    value = models.DecimalField(
        verbose_name='Valor do Empréstimo Pretendido',
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )
    status = models.CharField(max_length=255, default='pending')

    def __str__(self):
        return f'<Proposal id:{self.id}, name:{self.name}, value:{self.value}, status:{self.status}>'
