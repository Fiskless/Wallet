from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Wallet(models.Model):

    title = models.CharField('название кошелька', max_length=50)
    balance = models.DecimalField('баланс кошелька',
                                max_digits=8,
                                decimal_places=2,
                                validators=[MinValueValidator(0)])
    owner = models.ForeignKey(User, verbose_name='владелец кошелька', on_delete=models.CASCADE, related_name='wallets')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'кошелек'
        verbose_name_plural = 'кошельки'


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, verbose_name='кошелек', on_delete=models.CASCADE)
    data = models.DateTimeField('дата транзакции', auto_now_add=True)
    sum = models.DecimalField('сумма транзакции',
                                max_digits=8,
                                decimal_places=2,)
    comment = models.CharField('комментарий к транзакции',
                                max_length=200, null=True, blank=True)
    user = models.ForeignKey(User,
                             verbose_name='пользователь, совершающий транзакцию',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.wallet.title

    class Meta:
        verbose_name = 'транзакция'
        verbose_name_plural = 'транзакции'


