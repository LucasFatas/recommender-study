import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import  spotifyLogo from "../assets/spotifyIcon.svg"

const SpotifyUrl = 'https://accounts.spotify.com/authorize?response_type=code&client_id=8073ee0f16a64774bd0e7f8fa955b9d6&redirect_uri=http://localhost:3000/callback&scope=user-top-read'




export const LoginPage = () => {

    
const [clicked, setClicked] = useState(false);

useEffect(() => {
  if (clicked) {
    // do something meaningful, Promises, if/else, whatever, and then
    window.location.assign(SpotifyUrl);
  }
});
    

return (
   
        <div className='grid place-items-center h-screen'>
            <div className="flex items-center justify-center w-fit mt-5 space-x-7 ">
            
                <button className="  bg-green-500 hover:bg-green-700 text-lg text-white font-bold py-2 px-4 rounded-full " onClick={() => setClicked(true)} >
                    <div className='grid place-items-center '>
                        <img src={spotifyLogo} alt="Spotify Logo" class="filter-green" />
                        <span className="text-black"> Login to Spotify </span>
                    </div>
                </button> 
            
            </div>
        </div>
      

)
}