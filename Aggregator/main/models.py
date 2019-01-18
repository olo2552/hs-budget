from django.db import models

class BudgetItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    when = models.DateTimeField()

    class Meta:
        abstract = True

class Income(BudgetItem):
    pass

class Expense(BudgetItem):
    pass
