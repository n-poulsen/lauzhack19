import React from 'react'
import { StyleSheet, View, Text, FlatList } from 'react-native'
import { connect } from 'react-redux'
import SampleItem from './SampleItem'

class History extends React.Component {

    constructor(props) {
        super(props)
        this._displaySamples = this._displaySamples.bind(this)

        this.state = {
            all_samples: [],
            isLoading: true
        }

        this.state.all_samples = fetch('http://127.0.0.1:8000/api/loadAllSamples/')
            .then((response) => response.json())
            .then((data) => {
                this.setState({ all_samples: data.samples }, () => {
                    console.log('All Samples: ', this.state.all_samples);
                    this.state.isLoading = false
                })
            }).catch((error) => console.error(error));
    }

    _displaySampleHistory = (sampleId) => {
        console.log('navig to Sample')
        this.props.navigation.navigate('SampleHistory', { sampleId: sampleId })
    }

    _displayFlatList() {
        if (this.state.all_samples != []) {
            return (
                <FlatList
                    style={styles.list}
                    data={this.state.all_samples}
                    keyExtractor={(item) => item.sample_name}
                    renderItem={({ item }) => (
                        < SampleItem
                            sample={item}
                            displaySampleHistory={this._displaySampleHistory}
                        />
                    )}
                >
                </FlatList>
            )
        }
        else {
            return (<Text>No history</Text>)
        }
    }

    _displaySamples() {
        if (this.state.all_samples != []) {
            return (
                <View>
                    <View style={styles.tab_description}>
                        <Text style={styles.text}> NAME </Text>
                        <Text style={styles.text}> DANGER</Text>
                        <Text style={styles.text}> TYPE</Text>
                    </View>
                    <FlatList
                        style={styles.list}
                        data={this.state.all_samples}
                        keyExtractor={(item) => item.sample_name}
                        renderItem={({ item }) => (
                            < SampleItem
                                sample={item}
                                displaySampleHistory={this._displaySampleHistory}
                            />
                        )}
                    >
                    </FlatList>
                </View >
            )
        }
    }

    render() {
        console.log('render', this.props.sampleList)
        return (
            <View style={styles.main_container}>
                {this._displaySamples()}
            </View>
        )

    }
}

const mapStateToProps = (state) => {
    console.log("history state", state)
    return {
        sampleList: state.sampleList.flat()
    }
}

export default connect(mapStateToProps)(History)

const styles = StyleSheet.create({
    main_container: {
        flex: 1,
    },
    tab_description: {
        flexDirection: 'row',
        justifyContent: 'space-around'
    },
    text: {
        fontWeight: 'bold'
    }
})