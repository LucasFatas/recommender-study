export default class APIService{
    // Send the answers
    static sendAnswer(body){
        
        const mapToObject = Object.fromEntries(body);

        return fetch(`http://localhost:5000/saveAnswer`,{
            method :'POST',
            mode : 'no-cors',
            headers : {
                'Content-Type':'application/json'
            },
            body: JSON.stringify(mapToObject),
        })
        .then(response => {console.log(response)})
        .catch(error => console.log(error))
    }

}