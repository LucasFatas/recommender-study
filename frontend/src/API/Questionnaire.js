import * as server from '../util/API.json';

const { serverUrl, port } = server;

// Send the answers
export const sendAnswer = async (body) => {
    
    const mapToObject = Object.fromEntries(body);

    try {
        const response = await fetch(`${serverUrl}:${port}/saveAnswer`, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(mapToObject),
        });
        console.log(response);
    } catch (error) {
        return console.log(error);
    }
}