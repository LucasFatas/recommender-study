import React from "react";
import { StarRating } from "./StarRating";

export const Playlist = ({name}) => {


    return (
        <div>
            <h2>{ name }</h2>
                    <div>
                        <h3>Song 1</h3>
                        <StarRating/>
                    </div>
                    
                    <div>
                        <h3>Song 2</h3>
                        <StarRating/>
                    </div>

                    <div>
                        <h3>Song 3</h3>
                        <StarRating/>
                    </div>
                    <div>
                        <h3>Song 4</h3>
                        <StarRating/>
                    </div>
                    <div>
                        <h3>Song 5</h3>
                        <StarRating/>
                    </div>

        </div>
    )
}