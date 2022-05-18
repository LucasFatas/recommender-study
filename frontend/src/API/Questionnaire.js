const {serverUrl, port} = require('../util/API.json');

// Send the answers
export const sendAnswer = async (body) => {
    
    const mapValuesToArr = Array.from(body.values());
    const obj = {
        user : 123,
        personality_answers : [],
        value_answers : mapValuesToArr
    }

    try {
        const response = await fetch(`${serverUrl}:${port}/saveAnswer`, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(obj),
        });
        console.log(response);
    } catch (error) {
        return console.log(error);
    }
}