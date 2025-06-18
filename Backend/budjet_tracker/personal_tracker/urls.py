from django.urls import path, include
from rest_framework.routers import DefaultRouter
from personal_tracker.budjet_views import CategoryViewSet, TransactionViewSet, MonthlyBudgetViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet,basename='categories')
router.register(r'transactions', TransactionViewSet,basename='transactions')
router.register(r'budgets', MonthlyBudgetViewSet,basename='budgets')

urlpatterns = [
    path('', include(router.urls)),
]
