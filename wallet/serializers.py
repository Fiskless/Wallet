from rest_framework import serializers
from .models import Wallet, Transaction


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ['id', 'title', 'balance']


class WalletDetailSerializer(serializers.ModelSerializer):
    balance = serializers.ReadOnlyField()

    class Meta:
        model = Wallet
        fields = ['id', 'title', 'balance']


class TransactionWalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'data', 'sum', 'comment']
    #
    # def get_transaction(self, owner):
    #     return Transaction.objects.filter(user=owner)


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'wallet', 'data', 'sum', 'comment']


