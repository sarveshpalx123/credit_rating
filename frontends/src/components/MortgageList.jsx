import React, { useEffect, useState } from "react";
import { getMortgages, deleteMortgage, updateMortgage } from "../api";

const MortgageList = () => {
  const [mortgages, setMortgages] = useState([]);
  const [editingMortgage, setEditingMortgage] = useState(null);
  const [formData, setFormData] = useState({});

  useEffect(() => {
    fetchMortgages();
  }, []);

  const fetchMortgages = async () => {
    const data = await getMortgages();
    setMortgages(data);
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleEdit = (mortgage) => {
    setEditingMortgage(mortgage.id);
    setFormData(mortgage);
  };

  const handleUpdate = async () => {
    await updateMortgage(editingMortgage, formData);
    setEditingMortgage(null);
    fetchMortgages();
  };

  const handleDelete = async (id) => {
    await deleteMortgage(id);
    fetchMortgages();
  };

  return (
    <div className="container mt-3">
      <h4 className="mb-3 text-center">Mortgage List</h4>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>No.</th>
            <th>Credit Score</th>
            <th>Loan Amount</th>
            <th>Property Value</th>
            <th>Annual Income</th>
            <th>Debt Amount</th>
            <th>Loan Type</th>
            <th>Property Type</th>
            <th>Credit Rating</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {mortgages.map((mortgage, index) => (
            <tr key={mortgage.id}>
              <td>{index + 1}</td>
              
              {/* Editable Fields */}
              {editingMortgage === mortgage.id ? (
                <>
                  <td>
                    <input
                      type="number"
                      name="credit_score"
                      value={formData.credit_score}
                      onChange={handleChange}
                      className="form-control"
                    />
                  </td>
                  <td>
                    <input
                      type="number"
                      name="loan_amount"
                      value={formData.loan_amount}
                      onChange={handleChange}
                      className="form-control"
                    />
                  </td>
                  <td>
                    <input
                      type="number"
                      name="property_value"
                      value={formData.property_value}
                      onChange={handleChange}
                      className="form-control"
                    />
                  </td>
                  <td>
                    <input
                      type="number"
                      name="annual_income"
                      value={formData.annual_income}
                      onChange={handleChange}
                      className="form-control"
                    />
                  </td>
                  <td>
                    <input
                      type="number"
                      name="debt_amount"
                      value={formData.debt_amount}
                      onChange={handleChange}
                      className="form-control"
                    />
                  </td>
                  <td>
                    <select
                      name="loan_type"
                      value={formData.loan_type}
                      onChange={handleChange}
                      className="form-control"
                    >
                      <option value="fixed">Fixed</option>
                      <option value="adjustable">Adjustable</option>
                    </select>
                  </td>
                  <td>
                    <select
                      name="property_type"
                      value={formData.property_type}
                      onChange={handleChange}
                      className="form-control"
                    >
                      <option value="single_family">Single Family</option>
                      <option value="condo">Condo</option>
                    </select>
                  </td>
                  <td>{mortgage.credit_rating}</td>
                </>
              ) : (
                <>
                  <td>{mortgage.credit_score}</td>
                  <td>{mortgage.loan_amount}</td>
                  <td>{mortgage.property_value}</td>
                  <td>{mortgage.annual_income}</td>
                  <td>{mortgage.debt_amount}</td>
                  <td>{mortgage.loan_type}</td>
                  <td>{mortgage.property_type}</td>
                  <td>{mortgage.credit_rating}</td>
                </>
              )}

              {/* Action Buttons */}
              <td>
                {editingMortgage === mortgage.id ? (
                  <button onClick={handleUpdate} className="btn btn-success btn-sm me-2">
                    Save
                  </button>
                ) : (
                  <button onClick={() => handleEdit(mortgage)} className="btn btn-primary btn-sm me-2">
                    Edit
                  </button>
                )}
                <button onClick={() => handleDelete(mortgage.id)} className="btn btn-danger btn-sm">
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MortgageList;
