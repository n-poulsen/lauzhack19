import React from 'react';
import { Provider } from 'react-redux'
import Navigation from './Navigations/Navigation'
import Store from './Store/configureStore'
import {Dimensions, View} from 'react-native'

export default function App() {

  return (
    <View style={{marginLeft: 200, marginRight: 200, marginTop: 10}}>
      <Provider store={Store}>
        <Navigation />
      </Provider>
    </View>
  );
}

