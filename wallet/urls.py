from django.urls import path
from . import views

app_name = "wallet"

urlpatterns = [
    path('wallets/', views.WalletList.as_view()), # Список всех кошельков, также можно создать кошелек
    path('wallets/transactions/', views.TransactionWallet.as_view()), # Список транзакций для всех кошельков
    path('wallet/<int:pk>/', views.WalletRetrieveUpdateDestroy.as_view()), # Данные 1 кошелька, также есть возможность удалить или редактировать кошелек
    path('wallet/<int:pk>/transactions/', views.TransactionCreateWallet.as_view()), # Список транзакций для 1 кошелька, также есть возможность создания транзакции
    path('wallet/<int:pk>/transaction/<int:id>/', views.TransactionRetrieveDestroy.as_view()), # # Данные 1 транзакции, также есть возможность удалить транзакцию
]