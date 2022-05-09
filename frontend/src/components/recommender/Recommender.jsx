import React from "react";
import { Playlist } from "./Playlist";

export const Recommender = () => {


    return (
        <div className='grid place-items-center'>
            <div className="flex justify-center w-fit mt-10 space-x-7 ">
                {/* <div className=' w-70  border-2 border-sky-500 '> */}
                    
                <Playlist
                name="Playlist 1"
                />
                <Playlist
                name="Playlist 2"
                />
                <Playlist
                name="Playlist 2"
                />
                
                
            </div>
            
            <textarea autofocus required placeholder="type your message" maxlength="180"  cols="50" rows="6" wrap="hard"
            className=' mt-10 border-2 border-sky-500 '>
            </textarea>
        </div>
    )
}