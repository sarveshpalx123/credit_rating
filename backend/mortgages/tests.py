from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Mortgage

class MortgageAPITestCase(TestCase):
    """ Unit tests for the Mortgage API """

    def setUp(self):
        """ Set up test client and sample data before each test """
        self.client = APIClient()
        self.valid_data = {
            "credit_score": 720,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 80000,
            "debt_amount": 20000,
            "loan_type": "fixed",
            "property_type": "single_family",
        }
        self.invalid_data = {
            "credit_score": 200,  # Invalid credit score (should be between 300-850)
            "loan_amount": -50000,  # Negative loan amount
            "property_value": 0,  # Property value cannot be zero
            "annual_income": 0,  # Annual income cannot be zero
            "debt_amount": -10000,  # Negative debt amount
            "loan_type": "invalid_type",  # Invalid loan type
            "property_type": "invalid_type",  # Invalid property type
        }

    def test_create_valid_mortgage(self):
        """ Test creating a valid mortgage (should return HTTP 201) """
        response = self.client.post('/api/mortgages/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('credit_rating', response.data)

    def test_create_invalid_mortgage(self):
        """ Test creating a mortgage with invalid data (should return HTTP 400) """
        response = self.client.post('/api/mortgages/', self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_mortgage_list(self):
        """ Test retrieving all mortgages (should return HTTP 200) """
        response = self.client.get('/api/mortgages/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_mortgage_detail_not_found(self):
        """ Test retrieving a non-existent mortgage (should return HTTP 404) """
        response = self.client.get('/api/mortgages/999/')  # ID 999 does not exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)








import unittest
from django.test import TestCase
from mortgages.views import calculate_credit_rating

class CreditRatingTestCase(unittest.TestCase):
    
    def test_low_risk_scenario(self):
        """Test for a low-risk mortgage (should return 'AAA')"""
        data = {
            'loan_amount': 900000,  # High loan
            'property_value': 1000000,  # Property value
            'debt_amount': 50000,  # Low debt
            'annual_income': 200000,  # High income
            'credit_score': 700,  # Good credit score
            'loan_type': 'fixed',  # Lower risk
            'property_type': 'single_family'  # No risk increase
        }
        self.assertEqual(calculate_credit_rating(data), "AAA")

    def DTI(self):
        data = {
        'loan_amount': 500000,
        'property_value': 600000,  # LTV = 0.83 (Adds 1 risk)
        'debt_amount': 100000,
        'annual_income': 250000,  # DTI = 0.4 (Adds 1 risk)
        'credit_score': 650,  # No risk change
        'loan_type': 'fixed',  # Reduces risk by 1
        'property_type': 'condo'  # Adds 1 risk
    }
        self.assertEqual(calculate_credit_rating(data), "AAA")


    def DTI(self):
        data = {
        'loan_amount': 500000,
        'property_value': 600000,  # LTV = 0.83 (Adds 1 risk)
        'debt_amount': 100000,
        'annual_income': 250000,  # DTI = 0.4 (Adds 1 risk)
        'credit_score': 650,  # No risk change
        'loan_type': 'fixed',  # Reduces risk by 1
        'property_type': 'condo'  # Adds 1 risk
    }
        self.assertEqual(calculate_credit_rating(data), "AAA")


    def test_medium_risk_scenario(self):
        """Test for a medium-risk mortgage (should return 'BBB')"""
        data = {
            'loan_amount': 180000,
            'property_value': 200000,  # LTV = 90%
            'debt_amount': 45000,
            'annual_income': 100000,  # DTI = 45%
            'credit_score': 680,
            'loan_type': 'adjustable',
            'property_type': 'condo'
        }
        self.assertEqual(calculate_credit_rating(data), "BBB")


    def test_high_risk_scenario(self):
        """Test for a high-risk mortgage (should return 'C')"""
        data = {
            'loan_amount': 190000,
            'property_value': 200000,  # LTV = 95%
            'debt_amount': 60000,
            'annual_income': 100000,  # DTI = 60%
            'credit_score': 620,
            'loan_type': 'adjustable',
            'property_type': 'condo'
        }
        self.assertEqual(calculate_credit_rating(data), "C")


    def test_credit_score_edge_cases(self):
        """Test edge cases for credit scores"""
        self.assertEqual(calculate_credit_rating({
            'loan_amount': 100000,
            'property_value': 200000,  # LTV = 50%
            'debt_amount': 30000,
            'annual_income': 100000,  # DTI = 30%
            'credit_score': 700,
            'loan_type': 'fixed',
            'property_type': 'single_family'
        }), "AAA")
        
        self.assertEqual(calculate_credit_rating({
            'loan_amount': 100000,
            'property_value': 200000,  # LTV = 50%
            'debt_amount': 30000,
            'annual_income': 100000,  # DTI = 30%
            'credit_score': 649,
            'loan_type': 'fixed',
            'property_type': 'single_family'
        }), "BBB")
    
    
    
    
    

    
    
if __name__ == '__main__':
    unittest.main()
