const { serverUrl, port } =  require('../util/API.json');
const { parseSessionObj, orderAnswers } = require('../controller/questionnaireController');

//TODO: remove 2 arrays below when properly implemented
const value_answers =  Array(40).fill().map(() => Math.floor(Math.random() * 6) + 1);
const personality_answers =  Array(60).fill().map(() => Math.floor(Math.random() * 5) + 1);

// Send the answers
export const sendAnswer = async (navigate, setLoading, setResults) => {

    const userID = sessionStorage.getItem('userID');
    //const userID = Math.floor(Math.random() * 10000); //TODO: remove, used for debug
    
    if (userID === null) {
        navigate("/error/login");
        return;
    }
    
    //TODO : uncomment beofre deploying, remove hard-coded values
    
    /* const answers = sessionStorage.getItem("answers");
    const parsedAnswers = parseSessionObj(JSON.parse(answers));
    const body = orderAnswers(parsedAnswers);
    const personalityArray = Array.from(body.personality.values());
    const valuesArray = Array.from(body.values.values());
    
    const obj = {
        user : userID,
        personality_answers : personalityArray,
        value_answers : valuesArray
    } */

    const obj = {
        user : userID,
        personality_answers : personality_answers,
        value_answers : value_answers
    }


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