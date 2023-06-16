from django.db import models
from cpf_field.models import CPFField


class Proposal(models.Model):

    class StatusChoices(models.TextChoices):
        APPROVED = 'approved', 'Aprovado'
        REFUSED = 'refused', 'Recusado'
        PENDING = 'pending', 'Pendente'

    name = models.CharField(
        verbose_name='Nome Completo', max_length=255, null=False, blank=False
    )
    cpf = CPFField(verbose_name='CPF', null=False, blank=False)
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
    status = models.CharField(
        max_length=255,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )

    def __str__(self):
        return f'<Proposal id:{self.id}, name:{self.name}, value:{self.value}, status:{self.status}>'
