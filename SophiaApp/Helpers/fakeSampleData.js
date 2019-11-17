
const samples = [
    {
        sample_name: "room1",
        danger: 0,
        origin: 'room',
        date: '17/09',
        organisms_found: [
            {
                name: 'virus1',
                type: 'virus',
                confidence: 80,
                danger: 1
            },
            {
                name: 'virus2',
                type: 'virus',
                confidence: 80,
                danger: 2
            }
        ]
    },
    {
        sample_name: "pat2",
        danger: 0,
        origin: 'patient',
        date: 'string',
        organisms_found: [
            {
                name: 'virus1',
                type: 'virus',
                confidence: 80,
                danger: 1
            }
        ]
    }
]

export default samples