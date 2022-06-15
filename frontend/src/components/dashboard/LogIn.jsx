import React from "react";
import { useState } from "react";
import { useNavigate } from 'react-router-dom';
import { useEffect } from "react";
import { logIn } from "../../API/Dashboard";


export const LogIn = () => {

  const navigate = useNavigate();

  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");
  
  const [errorLogIn, setErrorLogIn] = useState(false);

  const handleSubmit = async e => {
    e.preventDefault();
    const token = await logIn({
      username,
      password
    });
    if(token instanceof Error || !token) {
      console.log("wrong authentification");
      setErrorLogIn(true);
    }
    else {
      sessionStorage.setItem("token", token); 
      navigate("/dashboard");
    }
  }

  useEffect(() => {
    const token = sessionStorage.getItem("token");
    if (token)
      navigate("/dashboard")
  });
  



  return(
  <div className='flex flex-col items-center justify-between py-28 text-center'>
    <h1 className="text-xl w-1/3">Welcome to the login page for the researcher dashboard, please login with the provided credentials to access the dashboard.</h1>
    <form onSubmit={handleSubmit}>
      <label className="flex items-center py-8">
        <input placeholder="Username" className="mt-1 block  px-6 py-3 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
        focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500" type="text" onChange={e => setUserName(e.target.value)}/>
      </label>
      <label className="flex items-center pb-8">
        <input placeholder="Password" className="mt-1 block  px-6 py-3 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
    focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500" type="password" onChange={e => setPassword(e.target.value)}/>
      </label>
      <div className="text-center">
        <button className={`${errorLogIn ? "animate-bounce bg-red-500 hover:bg-red-700" : ""} bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full`} type="submit">Submit</button>
      </div>
    </form>
  </div>
  )
}