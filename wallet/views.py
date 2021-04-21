from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionWalletSerializer, WalletDetailSerializer, TransactionSerializer


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
        return serializer.save(user=self.request.user, wallet=wallet)


class TransactionWallet(generics.ListAPIView):

    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)
