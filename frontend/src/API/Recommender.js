import * as server from '../util/API.json';

const { serverUrl, port } = server;

export const sendRatings = async (ratings) => {
    console.log(ratings);
    try {
        const response = await fetch(`${serverUrl}:${port}/ratings/add`, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(ratings),
        });
        console.log(response);
    } catch (error) {
        return console.log(error);
    }
}