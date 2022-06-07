import * as server from '../util/API.json';

const { serverUrl, port } = server;

// Send the answers
export const sendAnswer = async (body) => {
    
    const personalityArray = Array.from(body.personality.values());
    const valuesArray = Array.from(body.values.values());
    const obj = {
        user : 1,
        personality_answers : personalityArray,
        values_answers : valuesArray
    }

    console.log(obj);

    try {
        await fetch(`${serverUrl}:${port}/questionnaire/answer/add`, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(obj),
        })
        .then(res => res.json())
        .then(data => sessionStorage.setItem("questionnaireResults", JSON.stringify(data)))
        
    } catch (error) {
        return console.log(error);
    }
}