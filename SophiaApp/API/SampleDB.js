import sampleData from '../Helpers/fakeSampleData'

export function getFakeSample(sample) {
    if ((ind = sampleData.findIndex(n => n.sample_name == sample.toString())) != -1) {
        console.log('found', sampleData[ind])
        return sampleData[ind]
    }
    else {
        console.log('not found')
        return []
    }
}


const url = 'http://127.0.0.1:8000/';

export function getAllSample() {
    return fetch('http://127.0.0.1:8000/api/loadAllSamples/')
        .then((response) => response.json())
        .catch((error) => console.error(error))
}

/*
export function getSample(sample) {
    return fetch('http://127.0.0.1:8000/api/loadSample/?sample=' + sample)
        .then((response) => { return response })
        .then(function (data) {
            const items = data;
            console.log(items)
        })
        .catch((error) => console.error(error))
}*/

export function addSample(sample) {
    fetch(url + 'api/addSample/', {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'url': sample,
        }),
    });
}

export function getSample(sample) {
    fetch('http://127.0.0.1:8000/api/loadSample/?sample=' + sample)
        .then((response) => response.json())
        .then(function (data) {
            const items = data;
            console.log(items)
            return items
        })
        .catch((error) => console.error(error));
}