from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Mortgage
from .serializers import MortgageSerializer
import logging


# Setup logger
logger = logging.getLogger(__name__)

def calculate_credit_rating(data):
    risk_score = 0

    # Loan-to-Value Ratio (LTV)
    ltv = data['loan_amount'] / data['property_value']
    if ltv > 0.9:
        risk_score += 2
    elif ltv > 0.8:
        risk_score += 1

    # Debt-to-Income Ratio (DTI)
    dti = data['debt_amount'] / data['annual_income']
    if dti > 0.5:
        risk_score += 2
    elif dti > 0.4:
        risk_score += 1

    # Credit Score
    if data['credit_score'] >= 700:
        risk_score -= 1
    elif data['credit_score'] < 650:
        risk_score += 1

    # Loan Type
    if data['loan_type'] == 'fixed':
        risk_score -= 1
    else:
        risk_score += 1

    # Property Type
    if data['property_type'] == 'condo':
        risk_score += 1

    # Assign Credit Rating
    if risk_score <= 2:
        return 'AAA'
    elif 3 <= risk_score <= 5:
        return 'BBB'
    else:
        return 'C'

@api_view(['GET', 'POST'])
def mortgage_list_create(request):
    logger.info("Fetching all mortgage records")
    if request.method == 'GET':
        mortgages = Mortgage.objects.all()
        serializer = MortgageSerializer(mortgages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        logger.info(f"Received mortgage data: {request.data}")
        serializer = MortgageSerializer(data=request.data)
        if serializer.is_valid():
            
            data = serializer.validated_data
            
            credit_rating = calculate_credit_rating(data)  # Compute rating
            
            serializer.save(credit_rating=credit_rating)
            logger.info(f"Mortgage created with credit rating: {credit_rating}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        logger.error(f"Mortgage creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def mortgage_detail(request, pk):
    try:
        mortgage = Mortgage.objects.get(pk=pk)
    except Mortgage.DoesNotExist:
        logger.warning(f"Mortgage ID {pk} not found")
        return Response({'error': 'Mortgage not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MortgageSerializer(mortgage)
        return Response(serializer.data)

    elif request.method == 'PUT':
        logger.info(f"Updating mortgage ID {pk} with data: {request.data}")
        serializer = MortgageSerializer(mortgage, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            credit_rating = calculate_credit_rating(data)
            serializer.save(credit_rating=credit_rating)
            logger.info(f"Mortgage ID {pk} updated with new credit rating: {credit_rating}")
            return Response(serializer.data)
        
        logger.error(f"Failed to update mortgage ID {pk}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        logger.info(f"Deleting mortgage ID {pk}")
        mortgage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
