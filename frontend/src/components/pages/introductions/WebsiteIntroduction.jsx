import React from "react";
import { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import  spotifyLogo from "../../../assets/spotifyLogo.svg"
import { websiteIntroductionSecurity } from "../../../controller/pathSecurityController";

export const WebsiteIntroduction = (props) => {

  const {
    data
  } = props;

  
  const url = useLocation().pathname

  const callback =  data.serverUrl + ':' + data.port + '/spotify/callback&scope=user-top-read';
  const SpotifyUrl = `https://accounts.spotify.com/authorize?response_type=code&client_id=8073ee0f16a64774bd0e7f8fa955b9d6&redirect_uri=${callback}`;

  const [clicked, setClicked] = useState(false);

  const buttonStyleActive = "bg-green-500 hover:bg-green-700 text-lg text-white font-bold py-2 px-4 rounded-full";

  const navigate = useNavigate();



  
  useEffect(() => {
   websiteIntroductionSecurity(navigate)

  }, []);

  useEffect(() => {
    if (clicked) {
      sessionStorage.setItem("currentUrl", "/introduction")
      window.location.assign(SpotifyUrl);
    }
  })
  return (

    <div className='flex flex-col items-center justify-center h-screen w-screen'>
      <h1 className="text-4xl">RecMix</h1>
      <div className="w-1/2 h-1/2 overflow-y-scroll my-20">
        <p>
          Our experiment is about music recommendation. In order to conduct it, 
          we need some information about your musical preferences. This is why we will 
          ask you in the next page to log in your Spotify account. (We will only have access 
          to it this one time to retrieve the pieces of information we need).
        </p>
      </div>
      <div className="flex items-center justify-center">
        <button className={buttonStyleActive} onClick={() => setClicked(true)} >
          <div className='grid place-items-center'>
            <img src={spotifyLogo} alt="Spotify Logo" className="fill-white"/>
            <span className="text-black"> Login to Spotify </span>
          </div>
        </button> 
      </div>
    </div>
  )

}