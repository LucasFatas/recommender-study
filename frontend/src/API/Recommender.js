const { serverUrl, port } = require('../util/API.json');
const { buildDataObject } = require('../controller/recommenderController');

export const sendRatings = async (ratings, feedback) => {
    
    const userId = sessionStorage.getItem("userID");
    const tracklists = JSON.parse(sessionStorage.getItem("tracklists"));

    const data = buildDataObject(userId, ratings, tracklists, feedback);

    console.log(data);

    try {
        const response = await fetch(`${serverUrl}:${port}/spotify/ratings/add`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        }).then(res => res.json());
        console.log("add ratings : ", response);
    } catch (error) {
        console.log(error);
        return;
    }
}

export const getSongs = async (userId, setTracklists, setLoading) => {
    try {
        await fetch(`${serverUrl}:${port}/spotify/match?userId=${userId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(res => res.json())
        .then(data => {
            const [valMatch, persMatch, randMatch] = data.match;
            console.log(data);
            const tracklists = [
                {name : 'values', songs : valMatch.songs, matchedUserId : valMatch.user_id},
                {name : 'personality', songs : persMatch.songs, matchedUserId : persMatch.user_id},
                {name : 'random', songs : randMatch.songs, matchedUserId : randMatch.user_id}
            ];
            setTracklists(tracklists);
            sessionStorage.setItem("tracklists", JSON.stringify(tracklists));
        })
        .finally(() => setLoading(false))

    } catch (error) {
        console.log(error);
        return;
    }
}