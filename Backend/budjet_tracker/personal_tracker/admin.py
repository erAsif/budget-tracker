from django.contrib import admin
from .models import Category, Transaction, MonthlyBudget

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'amount', 'date')
    list_filter = ('user', 'category__type', 'date')
    search_fields = ('user__username', 'category__name')

@admin.register(MonthlyBudget)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'month', 'year', 'amount')
    list_filter = ('user', 'month', 'year')
    search_fields = ('user__username',)
