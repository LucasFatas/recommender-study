import * as server from '../util/API.json';

const { serverUrl, port } = server;

export const sendRatings = async (ratings) => {
    console.log(ratings);
    try {
        const response = await fetch(`${serverUrl}:${port}/spotify/ratings/add`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(ratings),
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

            const tracklists = [
                {name : 'values', songs : valMatch.songs},
                {name : 'personality', songs : persMatch.songs},
                {name : 'random', songs : randMatch.songs},
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