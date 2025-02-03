import api from './api';

export const fetchCompanies = async () => {
  const response = await api.get('companies/');
  return response.data;
};

export const addCompany = async (companyData) => {
  const response = await api.post('companies/', companyData);
  return response.data;
};
