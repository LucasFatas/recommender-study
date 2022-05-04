export default class APIService{
    // Send the answers
    static sendAnswer(body){
        return fetch(`http://145.94.183.106:5000/saveAnswer`,{
             method :'POST',
             crossDomain : true,
             mode : 'cors',
             headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify(body)
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }

}