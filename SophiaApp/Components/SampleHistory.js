import React from 'react'
import { StyleSheet, View, Text } from 'react-native'


export default class SampleHistory extends React.Component {
    render() {
        console.log('history sample props', this.props)
        return (
            < View >
                <Text>SampleHistoryViey</Text>
            </View >
        )
    }
}