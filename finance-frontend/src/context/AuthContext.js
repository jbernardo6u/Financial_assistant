// src/context/AuthContext.js
import React, { createContext, useState, useEffect } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Vérifie si un token JWT est présent dans le localStorage
    const token = localStorage.getItem('authToken');
    if (token) {
      // Décoder le token et définir l’utilisateur si valide
      setUser({ token });
    }
  }, []);

  const login = (token) => {
    localStorage.setItem('authToken', token);
    setUser({ token });
  };

  const logout = () => {
    localStorage.removeItem('authToken');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
