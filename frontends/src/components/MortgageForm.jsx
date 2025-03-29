import React, { useState } from "react";
import { addMortgage } from "../api";
import { useNavigate } from "react-router-dom";

const MortgageForm = () => {
  const [formData, setFormData] = useState({
    credit_score: "",
    loan_amount: "",
    property_value: "",
    annual_income: "",
    debt_amount: "",
    loan_type: "fixed",
    property_type: "single_family",
  });

  const [creditRating, setCreditRating] = useState(null);
  const [error, setError] = useState("");

  // Validation function
  const validateInput = () => {
    const { credit_score, loan_amount, property_value, annual_income, debt_amount } = formData;

    if (credit_score < 300 || credit_score > 850) return "Credit score must be between 300 and 850.";
    if (loan_amount <= 0) return "Loan amount must be a positive number.";
    if (property_value <= 0) return "Property value must be a positive number.";
    if (annual_income <= 0) return "Annual income must be a positive number.";
    if (debt_amount < 0) return "Debt amount cannot be negative.";

    return ""; // No errors
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    
    // Allow only numbers for numeric fields
    if (["credit_score", "loan_amount", "property_value", "annual_income", "debt_amount"].includes(name)) {
      if (!/^\d*$/.test(value)) return; // Allow only digits
    }

    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Perform validation
    const errorMsg = validateInput();
    if (errorMsg) {
      setError(errorMsg);
      return;
    }

    try {
      const data = await addMortgage(formData);
      setCreditRating(data.credit_rating);
      setError("");
    } catch (err) {
      setError("An error occurred while submitting the form.");
    }
  };

  return (
    <div className="container mt-4">
      <div className="row">
        {/* Left Box - Form */}
        <div className="col-md-8 p-4 bg-white shadow rounded">
          <h4 className="mb-3">Add Mortgage</h4>
          {error && <p className="text-danger">{error}</p>}
          <form onSubmit={handleSubmit}>
            <input
              type="number"
              name="credit_score"
              placeholder="Credit Score (300-850)"
              value={formData.credit_score}
              onChange={handleChange}
              className="form-control mb-3"
              min="300"
              max="850"
              required
            />
            <input
              type="number"
              name="loan_amount"
              placeholder="Loan Amount (Positive)"
              value={formData.loan_amount}
              onChange={handleChange}
              className="form-control mb-3"
              min="1"
              required
            />
            <input
              type="number"
              name="property_value"
              placeholder="Property Value (Positive)"
              value={formData.property_value}
              onChange={handleChange}
              className="form-control mb-3"
              min="1"
              required
            />
            <input
              type="number"
              name="annual_income"
              placeholder="Annual Income (Positive)"
              value={formData.annual_income}
              onChange={handleChange}
              className="form-control mb-3"
              min="1"
              required
            />
            <input
              type="number"
              name="debt_amount"
              placeholder="Debt Amount (0 or Positive)"
              value={formData.debt_amount}
              onChange={handleChange}
              className="form-control mb-3"
              min="0"
              required
            />
            <select name="loan_type" value={formData.loan_type} onChange={handleChange} className="form-control mb-3">
              <option value="fixed">Fixed</option>
              <option value="adjustable">Adjustable</option>
            </select>
            <select name="property_type" value={formData.property_type} onChange={handleChange} className="form-control mb-4">
              <option value="single_family">Single Family</option>
              <option value="condo">Condo</option>
            </select>
            <button type="submit" className="btn btn-primary w-100">Submit</button>
          </form>
        </div>

        {/* Right Box - Output */}
        <div className="col-md-4 p-4 bg-light shadow rounded">
          <h2 className="mb-3">Mortgage Details</h2>
          {creditRating ? (
            <p className="alert alert-success">Credit Rating: <strong>{creditRating}</strong></p>
          ) : (
            <p className="text-muted">Submit a mortgage to see results.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default MortgageForm;
