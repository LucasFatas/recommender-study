import * as server from '../util/API.json';

const { serverUrl, port } = server;

// Send the answers
export const sendAnswer = async (body) => {
    
    const mapValuesToArr = Array.from(body.values());
    const obj = {
        user : 1,
        personality_answers : [1, 2, 3],
        values_answers : mapValuesToArr
    }

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