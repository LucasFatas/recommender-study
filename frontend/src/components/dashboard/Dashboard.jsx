import React from "react";
import { useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import { isLogedIn } from "../../controller/dashboardController";


export const Dashboard = () => {

  const navigate = useNavigate()
 
  
    useEffect(() => {
      isLogedIn(sessionStorage.getItem("token"), navigate)
  
    }, [])

    const logout = () => {
      sessionStorage.removeItem("token")
      navigate("/login")
    }
    

  return (
    
    <div className='flex flex-col items-center justify-between py-28'>
      <h1> dashboard </h1>
      <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ' onClick={logout} >
        <div className='grid place-items-center '>
          <span className="text-white"> log out </span>
        </div>
      </button> 
    </div>
  )
}