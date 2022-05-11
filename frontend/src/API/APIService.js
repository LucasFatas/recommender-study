export default class APIService{
    // Send the answers
    static async sendAnswer(body){
        
        const mapValuesToArr = Array.from(body.values());
        const obj = {
            user : 1,
            personality_answers : [1, 2, 3],
            values_answers : mapValuesToArr
        }

        const url = "http://localhost:5000/";
        try {
            const response = await fetch(`${url}questionnaire/answer/add`, {
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

}