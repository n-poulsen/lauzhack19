import React from 'react'
import { StyleSheet, View, Text, Image } from 'react-native'
import VirusItem from './VirusItem'

export default class SampleHistory extends React.Component {

    constructor(props) {
        super(props)
        this.sampleid = undefined
        this.state = {
            sample: []
        }
    }

    componentDidMount() {
        console.log('dom0000000:');
        this.setState({ sample: [] });
        fetch('http://127.0.0.1:8000/api/loadSample/?sample=' + this.sampleid)
            .then((sample) => sample.json())
            .then((data) => this.setState({ sample: data }, () => { console.log('dom:', this.state.sample) }))
    }



    render() {
        console.log('sample id in shistory', this.sampleid = this.props.navigation.state.params.sampleId)
        if (this.sampleid != undefined) {
            const src = require("../Images/" + this.sampleid + ".png")
            return (
                < View style={{ alignItems: 'center', flex: 1, marginTop: 10 }}>
                    <Text style={styles.default_text}> Name: {this.state.sample.sample_name}</Text>
                    <Text style={styles.default_text}> Global danger: {this.state.sample.danger}</Text>
                    <Text style={styles.default_text}> Time: {this.state.sample.date}</Text>
                    <Image source={src} style={{ width: 400, height: 400 }} />
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
        fontStyle: 'italic'
    }
})
