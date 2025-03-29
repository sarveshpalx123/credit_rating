import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api/mortgages/";

// Get all mortgages
export const getMortgages = async () => {
  try {
    const response = await axios.get(BASE_URL);
    return response.data;
  } catch (error) {
    console.error("Error fetching mortgages:", error);
    return [];
  }
};

// Add a new mortgage
export const addMortgage = async (mortgageData) => {
  try {
    const response = await axios.post(BASE_URL, mortgageData);
    return response.data;
  } catch (error) {
    console.error("Failed to add mortgage:", error);
    throw error;
  }
};

// Update an existing mortgage
export const updateMortgage = async (id, updatedData) => {
  try {
    const response = await axios.put(`${BASE_URL}${id}/`, updatedData);
    return response.data;
  } catch (error) {
    console.error("Failed to update mortgage:", error);
    throw error;
  }
};

// Delete a mortgage
export const deleteMortgage = async (id) => {
  try {
    await axios.delete(`${BASE_URL}${id}/`);
  } catch (error) {
    console.error("Failed to delete mortgage:", error);
    throw error;
  }
};
