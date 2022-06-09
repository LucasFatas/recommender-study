const { serverUrl, port } =  require('../util/API.json');
const { parseSessionObj, orderAnswers } = require('../controller/questionnaireController');

//TODO: remove 2 arrays below when properly implemented
const value_answers =  [1, 2, 1, 4, 1, 1, 1, 5, 4, 3, 2, 1, 1, 6, 1, 1, 1, 6, 5, 1, 1, 6, 6, 1, 2, 1, 1, 6, 5, 2, 3, 4, 3, 1, 2, 4, 3, 1, 5, 1];
const personality_answers = [4, 1, 5, 4, 5, 5, 4, 3, 2, 1, 4, 1, 3, 1, 5, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 1, 5, 1, 1, 4, 2, 5, 5, 2, 5, 2, 4, 3, 4, 4, 3, 3, 3, 3, 3, 2, 2, 4, 2, 2, 5, 1, 2, 1, 4, 5, 2, 3, 4, 1];

// Send the answers
export const sendAnswer = async (navigate, setLoading, setResults) => {

    const userID = sessionStorage.getItem('userID');
    //const userID = Math.floor(Math.random() * 10000); //TODO: remove, used for debug
    
    if (userID === null) {
        navigate("/error/login");
        return;
    }
    
    //TODO : uncomment beofre deploying, remove hard-coded values
    
    const answers = sessionStorage.getItem("answers");
    const parsedAnswers = parseSessionObj(JSON.parse(answers));
    const body = orderAnswers(parsedAnswers);
    const personalityArray = Array.from(body.personality.values());
    const valuesArray = Array.from(body.values.values());
    
    const obj = {
        user : userID,
        personality_answers : personalityArray,
        value_answers : valuesArray
    }

    /* const obj = {
        user : userID,
        personality_answers : personality_answers,
        value_answers : value_answers
    } */


    try {
        await fetch(`${serverUrl}:${port}/questionnaire/answer/add`, {
            method: 'POST',
            headers: {
                "Access-Control-Allow-Origin": "localhost", //TODO: change to actual backend url
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(obj),
        })
        .then(res => res.json())
        .then(data => {
            const formatData = {...data, personality : data.personalities};
            setResults(formatData);
            sessionStorage.setItem("questionnaireResults", JSON.stringify(formatData));
            sessionStorage.setItem("answerSent", true);
        })
        .finally(() => setLoading(false));
        
    } catch (error) {
        console.log(error);
    }
}