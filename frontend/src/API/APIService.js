export default class APIService{
    // Send the answers
    static async sendAnswer(body){
        
        const mapToObject = Object.fromEntries(body);

        try {
            const response = await fetch(`http://localhost:5000/saveAnswer`, {
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

}