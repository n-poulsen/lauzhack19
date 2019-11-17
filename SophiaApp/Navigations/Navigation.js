
import { createStackNavigator } from 'react-navigation-stack'
import { createAppContainer } from 'react-navigation'
import { createMaterialTopTabNavigator } from 'react-navigation-tabs'
import Welcome from '../Components/Welcome'
import History from '../Components/History'
import SampleHistory from '../Components/SampleHistory'


const HistoryStackNavigator = createStackNavigator({
    History: {
        screen: History
    },
    SampleHistory: {
        screen: SampleHistory
    }
}
)

const VirusTabNavigator = createMaterialTopTabNavigator({
    History: {
        screen: HistoryStackNavigator,
        navigationOptions: {
            title: 'History',
            headerShown: false

        }
    },
    Welcome: {
        screen: Welcome,
        navigationOptions: {
            title: 'Welcome'
        }
    },
}, {
    initialRouteName: 'Welcome',
    tabBarOptions: {
        labelStyle: {
            fontSize: 20,
        }
    }
})

export default createAppContainer(VirusTabNavigator)