import React from 'react'
import { StyleSheet, View, Text } from 'react-native'
import { getSample } from '../API/SampleDB'

export default class SampleHistory extends React.Component {

    constructor(props) {
        super(props)
        this.sampleid = undefined
        this.state = {
            sample: []
        }
    }

    componentDidMount() {
        this.setState({sample: []});
        fetch('http://127.0.0.1:8000/api/loadSample/?sample=' + this.sampleid)
                        .then((sample) => sample.json())
                        .then((data) => this.setState({sample: data}));
    }

    render() {
        console.log('sample id in shistory', this.sampleid = this.props.navigation.state.params.sampleId)
        if (this.sampleid != undefined) {
            return (
                < View >
                    <Text> {this.state.sample.sample_name}</Text>
                   
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

})