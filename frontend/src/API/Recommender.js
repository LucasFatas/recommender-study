const { serverUrl, port } = require('../util/API.json');

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
    }
}