const url = 'http://127.0.0.1:8000/';

export function getAllSample() {
    return fetch(url + 'api/loadAllData/')
        .then((response) => response.json())
        .catch((error) => console.error(error))
}

export function getSample() {
    return fetch(url + 'api/loadSample/')
        .then((response) => response.json())
        .catch((error) => console.error(error))
}

export function addSample(sample) {

}