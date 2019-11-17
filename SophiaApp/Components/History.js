import React from 'react'
import { StyleSheet, View, Text, FlatList } from 'react-native'
import { connect } from 'react-redux'
import SampleItem from './SampleItem'

class History extends React.Component {

    constructor(props) {
        super(props)
        this._displaySamples = this._displaySamples.bind(this)


    }

    _displaySampleHistory = (sampleId) => {
        console.log('navig to Sample')
        this.props.navigation.navigate('SampleHistory', { sampleId: sampleId })
    }

    _displayFlatList() {
        if (sampleList != []) {
            return (
                <FlatList
                    style={styles.list}
                    data={this.props.sampleList}
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
        if (this.props.sampleList != []) {
            return (
                <View>
                    <View style={styles.tab_description}>
                        <Text style={styles.text}> NAME </Text>
                        <Text style={styles.text}> DANGER</Text>
                        <Text style={styles.text}> TYPE</Text>
                    </View>
                    <FlatList
                        style={styles.list}
                        data={this.props.sampleList}
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