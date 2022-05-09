import React from "react";
import { Playlist } from "./Playlist";

export const Recommender = () => {

const trackListRandom = ["https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad", 
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad",
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad",
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad",
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad"]
const trackListPersonality = ["https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad", 
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad",
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad",
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad",
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad"]
const trackListValue = ["https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad", 
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad",
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad",
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad",
										"https://open.spotify.com/embed/track/3IrPSIZXepPwIoKLQ4ADad"]
										

	return (
		<div className='grid place-items-center'>
			<div className="flex justify-center w-fit mt-10 space-x-7 ">
				{[trackListRandom, trackListPersonality, trackListValue].map((trackList, index) =>
					<Playlist
						name={"Playlist " +(index+1)}
						starSize="text-xl"
						trackList={trackList}
					/>
				)}
			</div>
			
			<textarea required placeholder="type your message" maxLength="180"  cols="50" rows="6" wrap="hard" className=' mt-10 border-2 border-sky-500 '/>
		</div>
	)
}