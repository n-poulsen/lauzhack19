import React from 'react'
import { StyleSheet, View, Text, Image } from 'react-native'

export default class VirusItem extends React.Component {

    constructor(props) {
        super(props)
        this.requireImage = '../Images/default_image.png'
    }

    _displayDangerImage() {

        const danger = this.props.virus.danger
        var color = 'green'
        if (danger == 1) {
            color = 'orange'
        }
        if (danger == 2) {
            color = 'red'
        }
        return (
            <Image
                style={[styles.image, { backgroundColor: color }]}
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
        justifyContent: 'space-around',
        borderBottomWidth: 2,
        paddingTop: 10
    },
    image: {
        width: 40,
        height: 30,
        marginBottom: 10,
    }
})