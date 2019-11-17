import React from 'react'
import { StyleSheet, SafeAreaView, View, TextInput, FlatList, Button, Text } from 'react-native'
import VirusItem from './VirusItem'
import { connect } from 'react-redux'
//import sampleData from '../Helpers/fakeSampleData'
import { getSample, getAllSample, addSample, getFakeSample } from '../API/SampleDB'

class Welcome extends React.Component {

    constructor(props) {
        super(props)
        this.searchedText = ''
        this.state = {
            sample: [],
            isLoading: false
        }
    }

    _displayFlatList(sample) {
        if (sample != [] && sample != undefined) {
            console.log("flatList displayed")
            return (
                <View style={styles.main_container}>
                    <FlatList
                        style={styles.list}
                        data={this._getOrganismesFoundFromSampleList(sample)}
                        renderItem={({ item }) => (
                            < VirusItem virus={item} />)}
                        keyExtractor={(item) => item.name}
                    />
                </View>)

        }
        else {
            return (
                <Text>No sample loaded</Text>
            )
        }
    }

    _getOrganismesFoundFromSampleList(sample) {
        console.log('sample data', sample)
        const res = sample.organisms_found
        return res

    }

    _loadSample(url) {
        fetch('http://127.0.0.1:8000/api/addSample/', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'url': url,
            }),
        })
        .then((response) => {
            const data = response.json()
            console.log(data);
            return data;
        }).then((data) => {
            this.setState({ sample: data.data }, () => {
                console.log('Sample: ', this.sample);
                this.isLoading = false;
            })
        });
        /*
        this.isLoading = true
        let tmp = addSample(url)
        console.log('tmp: ', tmp)
        this.setState({ sample: tmp }, () => {
            console.log('Sample: ', this.sample)
        })
        this.isLoading = false
        */
    }

    _searchTextInputChanged(text) {
        this.searchedText = text;
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
                    onChangeText={(text) => this._searchTextInputChanged(text)}
                    onSubmitEditing={() => this._loadSample} />
                <Button style={styles.bottom} title='Load Sample' onPress={() => { this._loadSample(this.searchedText) }} />
                {this._displayFlatList(this.state.sample)}
                {this._displayLoading()}
            </ SafeAreaView >
        )
    }
}

const mapStateToProps = (state) => {
    return {
        sample_data: state.sampleList.flat()
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