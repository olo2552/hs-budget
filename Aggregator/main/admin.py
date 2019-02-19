from django.contrib import admin
from main.models import Income, Expense


class BudgetItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'amount', 'when')


class ExpenseAdmin(BudgetItemAdmin):
    pass


class IncomeAdmin(BudgetItemAdmin):
    pass


admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
