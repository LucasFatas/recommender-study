export default class APIService{
    // Send the answers
    static sendAnswer(body){
        
        const obj = Object.fromEntries(body);
        console.log(obj);

        return fetch(`http://localhost:5000/saveAnswer`,{
             method :'POST',
             crossDomain : true,
             headers : {
                'Content-Type':'application/json'
            },
            body: JSON.stringify(obj),
        })
        .then(response => response.json())
        .catch(error => console.log(error))
    }

}