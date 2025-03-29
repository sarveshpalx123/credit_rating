# Mortgage Credit Rating System

## Description
A web-based application to evaluate mortgage credit risk based on Loan-to-Value (LTV), Debt-to-Income (DTI), Credit Score, Loan Type, and Property Type.

## Installation Instructions

### Backend Setup
1. Navigate to the backend directory:
   cd backend


python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows


pip install -r requirements.txt

python manage.py runserver



## Frontend Setup
cd frontend

npm start


# running the test 

cd backend
python manage.py test