import React from 'react'
import { StyleSheet, View, Text } from 'react-native'
import { getFakeSample } from '../API/SampleDB'

export default class SampleHistory extends React.Component {

    constructor(props) {
        super(props)
        this.sampleid = undefined
    }



    render() {
        console.log('sample id in shistory', this.sampleid = this.props.navigation.state.params.sampleId)
        if (this.sampleid != undefined) {
            return (
                < View >
                    <Text> {getFakeSample(this.sampleid).sample_name}</Text>
                    <Text> Danger Global: {getFakeSample(this.sampleid).danger}</Text>


                    <Image
                    >

                    </Image>
                </View >
            )
        }
        else {
            return (
                <View>
                    <Text>No sample</Text>
                </View>
            )
        }
    }
}

const styles = StyleSheet.create({
    default_text: {
        textAlign: 'justify'

    }
})