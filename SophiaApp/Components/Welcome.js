import React from 'react'
import { StyleSheet, SafeAreaView, View, TextInput, FlatList, Button, Text } from 'react-native'
import VirusItem from './VirusItem'
import { connect } from 'react-redux'
import sampleData from '../Helpers/fakeSampleData'
import { getAllSample } from '../API/SampleDB'

class Welcome extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            sample_data: getAllSample(),
            isLoading: false
        }
    }

    _getOrganismesFoundFromSampleList(samples) {
        console.log('sample data', samples)
        res = samples.map(sample => sample.organisms_found)
        return res.flat()
    }

    _loadSample() {
        console.log("load sample")
        // return sampleData for testing
        const action = { type: 'ADD_SAMPLE', value: sampleData }
        this.props.dispatch(action)
    }

    _displayLoading() {
        if (this.state.isLoading) {
            return (
                <View style={styles.loading_container}>
                    <ActivityIndicator size='large' />
                </View>
            )
        }
    }

    render() {
        return (
            < SafeAreaView style={styles.main_container} >
                <TextInput style={styles.textinput}
                    placeholder='Votre sample'
                    onSubmitEditing={() => this._loadSample} />
                <Button style={styles.bottom} title='Load Sample' onPress={() => { this._loadSample() }} />
                <Text> {this.state.sample_data.sample_name}</Text>
                <FlatList
                    style={styles.list}
                    data={this._getOrganismesFoundFromSampleList(this.state.sample_data)}
                    renderItem={({ item }) => (
                        < VirusItem virus={item} />)}
                    keyExtractor={(item) => item.name}
                />
                {this._displayLoading()}
            </ SafeAreaView >
        )
    }
}

const mapStateToProps = (state) => {
    return {
        sample_data: state.sampleList
    }
}

export default connect(mapStateToProps)(Welcome)

const styles = StyleSheet.create({
    main_container: {
        flex: 1,
    },
    textinput: {
        alignItems: 'center',
        paddingTop: 5,
        paddingBottom: 5,

    },
    bottom: {

    },
    loading_container: {
        position: 'absolute',
        left: 0,
        right: 0,
        top: 100,
        bottom: 0,
        alignItems: 'center',
        justifyContent: 'center'
    },
    list: {
        flex: 1,
        marginLeft: 10,
        marginRight: 10,
        marginEnd: 20,

    }
}
)