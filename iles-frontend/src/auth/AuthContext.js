import { createContext, useState } from "react";
import API from "../api/axios";
import { jwtDecode } from "jwt-decode";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  const login = async (username, password) => {
    try{
      const res = await API.post("users/login/", { username, password });

      localStorage.setItem("token", res.data.access);

      const decoded = jwtDecode(res.data.access);
      setUser({...decoded,role:res.data.role});
  }catch(error){
    console.log("LOGIN ERROR:",error.response.data);
  }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};