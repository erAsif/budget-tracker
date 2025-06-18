from rest_framework import serializers
from .models import Category, Transaction, MonthlyBudget

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        category_name = validated_data.pop('category')
        category = Category.objects.filter(name__iexact=category_name).first()
        if not category:
            raise serializers.ValidationError({'category': 'Category not found.'})
        return Transaction.objects.create(category=category, **validated_data)
    def update(self, instance, validated_data):
        category_name = validated_data.pop('category', None)
        if category_name:
            category = Category.objects.filter(name__iexact=category_name).first()
            if not category:
                raise serializers.ValidationError({'category': 'Category not found.'})
            instance.category = category

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.name
        return rep


class MonthlyBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyBudget
        fields = '__all__'
        read_only_fields = ['user']
