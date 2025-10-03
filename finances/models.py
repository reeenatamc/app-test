from django.db import models
from django.conf import settings

class CategoryTransaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    svg_image = models.ImageField(upload_to = 'category_icon')

    def __str__(self):
        return self.name

class Transaction(models.Model):
    class TransactionTypes(models.TextChoices):
        INCOME = "income", "Income"
        EXPENSE = "expense", "Expense"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        choices=TransactionTypes.choices,
        max_length=10,
        default=TransactionTypes.INCOME
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)
    category = models.ForeignKey(CategoryTransaction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.transaction_type} {self.amount} on {self.date}"


class Account(models.Model):
    class AccountTypes(models.TextChoices):
        GOAL = 'goal', 'Goal'
        SAVINGS = 'savings', 'Savings'
        NORMAL = 'normal', 'Normal'
        CUSTOM = 'custom', 'Custom'

    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(choices=AccountTypes.choices, max_length=10)

    def __str__(self):
        return f"{self.user} - {self.balance}"


