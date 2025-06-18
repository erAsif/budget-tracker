from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from datetime import date, timedelta
import calendar

from personal_tracker.models import Category, Transaction, MonthlyBudget
from personal_tracker.budjet_serializer import (
    CategorySerializer,
    TransactionSerializer,
    MonthlyBudgetSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        user = request.user
        time_filter = request.query_params.get('filter', 'monthly')

        today = date.today()
        if time_filter == 'weekly':
            start_date = today - timedelta(days=7)
        elif time_filter == 'yearly':
            start_date = today.replace(month=1, day=1)
        else:  # monthly
            start_date = today.replace(day=1)

        transactions = Transaction.objects.filter(user=user, date__gte=start_date)

        income = transactions.filter(category__type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = transactions.filter(category__type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
        balance = income - expense

        return Response({
            "total_income": income,
            "total_expense": expense,
            "remaining_balance": balance,
            "filter": time_filter
        })

class MonthlyBudgetViewSet(viewsets.ModelViewSet):
    serializer_class = MonthlyBudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MonthlyBudget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def compare(self, request):
        user = request.user
        today = date.today()
        month = int(request.query_params.get('month', today.month))
        year = int(request.query_params.get('year', today.year))

        try:
            budget = MonthlyBudget.objects.get(user=user, month=month, year=year)
            start_date = date(year, month, 1)
            end_date = date(year, month, calendar.monthrange(year, month)[1])
            expenses = Transaction.objects.filter(
                user=user,
                date__range=[start_date, end_date],
                category__type='expense'
            ).aggregate(Sum('amount'))['amount__sum'] or 0

            remaining = budget.amount - expenses

            return Response({
                "budgeted_amount": budget.amount,
                "actual_expense": expenses,
                "remaining_balance": remaining,
                "month": month,
                "year": year
            })

        except MonthlyBudget.DoesNotExist:
            return Response({"error": "Budget not set for this month."}, status=404)
