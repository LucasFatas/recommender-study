import React from "react";
import correctLogo from '../../assets/correctLogo.svg'

export const Thanks = () => {


  return (
    <div className='flex flex-col items-center justify-center h-screen w-screen '>
      <h3 className="text-4xl pd-5">THANK YOU</h3>
      <img src={correctLogo} alt="correct Logo" className="fill-white h-20" />
      <h2> Thank you for participating to this survey, you can now go back to prolifik with this code : XXXXXX </h2>
      
      
    </div>
  )
}