from rest_framework import serializers
from .models import Mortgage

class MortgageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortgage
        fields = '__all__'


    def validate_credit_score(self, value):
        if value < 300 or value > 850:
            raise serializers.ValidationError("Credit score must be between 300 and 850.")
        return value

    def validate_loan_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Loan amount must be a positive number.")
        return value

    def validate_property_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("Property value must be a positive number.")
        return value

    def validate_annual_income(self, value):
        if value <= 0:
            raise serializers.ValidationError("Annual income must be a positive number.")
        return value

    def validate_debt_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Debt amount cannot be negative.")
        return value

    def validate_loan_type(self, value):
        if value not in ['fixed', 'adjustable']:
            raise serializers.ValidationError("Loan type must be 'fixed' or 'adjustable'.")
        return value

    def validate_property_type(self, value):
        if value not in ['single_family', 'condo']:
            raise serializers.ValidationError("Property type must be 'single_family' or 'condo'.")
        return value
