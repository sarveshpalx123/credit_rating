from django.db import models
from django.core.exceptions import ValidationError


def validate_credit_score(value):
    if value < 300 or value > 850:
        raise ValidationError("Credit score must be between 300 and 850.")

def validate_positive(value):
    if value <= 0:
        raise ValidationError("This field must be a positive number.")


class Mortgage(models.Model):
        
    CREDIT_RATING_CHOICES = [
        ('AAA', 'AAA'),
        ('BBB', 'BBB'),
        ('C', 'C'),
    ]
        

    credit_score = models.IntegerField(validators=[validate_credit_score])
    loan_amount = models.FloatField(validators=[validate_positive])
    property_value = models.FloatField(validators=[validate_positive])
    annual_income = models.FloatField(validators=[validate_positive])
    debt_amount = models.FloatField(validators=[validate_positive])
    loan_type = models.CharField(max_length=10, choices=[('fixed', 'Fixed'), ('adjustable', 'Adjustable')])
    property_type = models.CharField(max_length=15, choices=[('single_family', 'Single Family'), ('condo', 'Condo')])
    credit_rating = models.CharField(max_length=3, choices=CREDIT_RATING_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id