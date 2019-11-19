import React from 'react'
import { StyleSheet, View, Text, Image, Dimensions } from 'react-native'

export default class VirusItem extends React.Component {

    constructor(props) {
        super(props)
        this.requireImage = '../Images/default_image.png'
    }

    _displayDangerImage() {

        const danger = this.props.virus.danger
        const confidence = this.props.virus.confidence
        var color = 'green'
        let wid = (Dimensions.get('window').width - 400) * (confidence / 100)
        if (danger == 1) {
            color = 'orange'
        }
        if (danger == 2) {
            color = 'red'
        }
        return (
            <Image
                style={[styles.image, { backgroundColor: color, width: wid }]}
                source={this.requiredImage}
            />
        )
    }

    render() {
        const { virus } = this.props
        return (
            <View style={styles.main_container} >
                <Text> {virus.name} </Text>
                {this._displayDangerImage()}
            </View>
        )
    }
}

const styles = StyleSheet.create({
    main_container: {
        flex: 1,
        flexDirection: 'row',
        justifyContent: 'space-between',
        paddingLeft: 20,
        paddingRight: 20,
        borderBottomWidth: 2,
        paddingTop: 10
    },
    image: {
        height: 30,
        marginBottom: 10,
    }
})