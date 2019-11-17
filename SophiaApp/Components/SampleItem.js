import React from 'react'
import { StyleSheet, TouchableOpacity, View, Text } from 'react-native'

export default class SampleItem extends React.Component {


    render() {
        console.log('sample item print')
        const { sample, displaySampleHistory } = this.props
        return (
            <TouchableOpacity
                style={styles.main_container}
                onPress={displaySampleHistory(sample.sample_name)}
            >
                <Text style={styles.text}> {sample.sample_name}</Text>
                <Text style={styles.text}>{sample.danger}</Text>
                <Text style={styles.text}>{sample.origin}</Text>

            </TouchableOpacity>
        )
    }
}

const styles = StyleSheet.create({
    main_container: {
        flex: 1,
        flexDirection: 'row',
        justifyContent: 'space-around',
        marginTop: 2,
        marginBottom: 2,
        paddingTop: 2,
        paddingBottom: 5,
        backgroundColor: '#D0D0D0'

    },
    text: {
        fontSize: 14
    }
}
)