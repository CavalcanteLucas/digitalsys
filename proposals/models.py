from django.db import models


class Proposal(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, default='pending')

    def __str__(self):
        return f'<Proposal id:{self.id}, name:{self.name}, value:{self.value}, status:{self.status}>'
