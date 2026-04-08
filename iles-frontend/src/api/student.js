// src/api/student.js
import API from "./axios"; // make sure axios.js exists in the same folder

export const getStudentLogs = () => API.get("logs/student/");
export const getStudentPlacement = () => API.get("internships/student/");
export const getStudentEvaluations = () => API.get("evaluations/student/");