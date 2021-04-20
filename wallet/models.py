from django.db import models
from django.core.validators import MinValueValidator


class Wallet(models.Model):
    title = models.CharField('название кошелька', max_length=50)
    balance = models.DecimalField('баланс кошелька',
                                max_digits=8,
                                decimal_places=2,
                                validators=[MinValueValidator(0)])
    price = models.DecimalField('сумма транзакции',
                                max_digits=8,
                                decimal_places=2,)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'кошелек'
        verbose_name_plural = 'кошельки'

