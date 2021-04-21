from django.urls import path
from . import views

app_name = "wallet"

urlpatterns = [
    path('wallets/', views.WalletList.as_view()),
    path('wallets/<int:pk>', views.WalletRetrieveUpdateDestroy.as_view()),
    path('wallets/transactions/', views.TransactionWallet.as_view()),
    path('wallets/<int:pk>/transactions/', views.TransactionCreateWallet.as_view()),
    # path('wallets/transactions/', views.WalletTransaction.as_view()),

]