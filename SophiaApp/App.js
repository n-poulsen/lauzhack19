import React from 'react';
import { Provider } from 'react-redux'
import Navigation from './Navigations/Navigation'
import Store from './Store/configureStore'
export default function App() {
  return (
    <Provider store={Store}>
      <Navigation />
    </Provider>
  );
}

