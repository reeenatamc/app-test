from django.contrib import admin
from unfold.admin import ModelAdmin

from finances.models import Transaction, Account, TransactionCategory

@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = ('user','amount', 'date')

@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_display = ('user', 'balance')

@admin.register(TransactionCategory)
class TransactionCategoryAdmin(ModelAdmin):
    list_display = ('user',)