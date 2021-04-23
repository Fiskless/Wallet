from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionWalletSerializer, WalletDetailSerializer, TransactionSerializer
from rest_framework.exceptions import ValidationError


class WalletList(generics.ListCreateAPIView):
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WalletRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WalletDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(owner=user)


class TransactionCreateWallet(generics.ListCreateAPIView):

    serializer_class = TransactionWalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        wallet = Wallet.objects.get(pk=self.kwargs['pk'])
        return Transaction.objects.filter(user=user, wallet=wallet)

    def perform_create(self, serializer):
        wallet = Wallet.objects.get(pk=self.kwargs['pk'])
        wallet.balance = wallet.balance + serializer.validated_data['sum']
        if wallet.balance < 0:
            raise ValidationError("You don't have enough money for this transaction(((")
        wallet.save()
        return serializer.save(user=self.request.user, wallet=wallet)


class TransactionWallet(generics.ListAPIView):

    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)


class TransactionRetrieveDestroy(generics.RetrieveAPIView, mixins.DestroyModelMixin):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        wallet = Wallet.objects.get(pk=self.kwargs['pk'])
        return Transaction.objects.get(id=self.kwargs['id'], user=user, wallet=wallet)

    def delete(self, request, *args, **kwargs):

        wallet = Wallet.objects.get(pk=self.kwargs['pk'])
        transaction_sum = Transaction.objects.get(id=self.kwargs['id'], user=self.request.user, wallet=wallet).sum
        wallet.balance = wallet.balance - transaction_sum
        wallet.save()
        return self.destroy(request, *args, **kwargs)
