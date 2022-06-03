import * as server from '../util/API.json';

const { serverUrl, port } = server;

export const sendRatings = async (ratings) => {
    console.log(ratings);
    try {
        const response = await fetch(`${serverUrl}:${port}/spotify/ratings/add`, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(ratings),
        });
        console.log(response);
    } catch (error) {
        console.log(error);
        return;
    }
}

export const getSongs = async (userId) => {
    try {
        const response = await fetch(`${serverUrl}:${port}/spotify/match?userId=${userId}`, {
            method: 'GET',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log(response);
    } catch (error) {
        console.log(error);
        return;
    }
}