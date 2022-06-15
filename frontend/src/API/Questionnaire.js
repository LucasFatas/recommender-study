const { serverUrl, port } =  require('../util/API.json');
const { parseSessionObj, orderAnswers } = require('../controller/questionnaireController');

// Send the answers
export const sendAnswer = async (navigate, setLoading, setResults) => {

    const userID = sessionStorage.getItem('userID');
    
    if (userID === null) {
        navigate("/error/login");
        return;
    }
    
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

    try {
        await fetch(`${serverUrl}:${port}/questionnaire/answer/add`, {
            method: 'POST',
            headers: {
                "Access-Control-Allow-Origin": "localhost",
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