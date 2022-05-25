import React from "react";
import { useState } from "react";
import { useNavigate } from 'react-router-dom';
import { useEffect } from "react";


export const LogIn = (props) => {

  const navigate = useNavigate();

  async function loginUser(credentials) {
    // return fetch('http://localhost:8080/login', {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   },
    //   body: JSON.stringify(credentials)
    // })
    //   .then(data => data.json())
    if(credentials.username === "user" && credentials.password === "pwd")
      return "test123"
    else 
      return ""
   }

  

  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async e => {
    e.preventDefault();
    const token = await loginUser({
      username,
      password
    });
    if(token === "")
      console.log("wrong authentification");
    else{
      sessionStorage.setItem("token", token); 
      console.log(token);
      navigate("/dashboard")
    }
  }

  useEffect(() => {
    const token = sessionStorage.getItem("token");
    if(token)
      navigate("/dashboard")
  });
  



  return(
    <div className="login-wrapper">
      <h1>Please Log In</h1>
      <form onSubmit={handleSubmit}>
        <label className="block">
          <p>Username</p>
          <input className="mt-1 block  px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
      focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500" type="text" onChange={e => setUserName(e.target.value)}/>
        </label>
        <label>
          <p>Password</p>
          <input className="mt-1 block  px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
      focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500" type="password" onChange={e => setPassword(e.target.value)}/>
        </label>
        <div>
          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" type="submit">Submit</button>
        </div>
      </form>
    </div>
  )
}