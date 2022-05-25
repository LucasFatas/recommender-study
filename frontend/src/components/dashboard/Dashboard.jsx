import React from "react";
import { useEffect } from "react";
import { useNavigate } from 'react-router-dom';


export const Dashboard = () => {

  const navigate = useNavigate()
 
  
    useEffect(() => {
      const token = sessionStorage.getItem("token");
      if(!token)
        navigate("/login")
      else
        console.log('success');
      
    }, [])

    const logout = () => {
      sessionStorage.removeItem("token")
      navigate("/login")
    }
    

  return (
    
    <div className='flex flex-col items-center justify-between h-screen w-screen py-28'>
      <h1> dashboard </h1>
      <button  onClick={logout} >
        <div className='grid place-items-center '>
          <span className="text-black"> next </span>
        </div>
      </button> 
    </div>
  )
}