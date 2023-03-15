import React from 'react'

import { BrowserRouter }from 'react-router-dom'
import { AppRoutes } from './routes/Routes'

import './App.css'

import { Header } from './shared/components/header/header'

function App() {

  return (
    <React.Fragment>
      
      <BrowserRouter>
        <div style={{display: 'flex',flexDirection: 'column', background: '#e8e8e8', width: '100vw', height: '100%'}}>
          <Header />
          <AppRoutes/>
        </div>
      </BrowserRouter>
    </React.Fragment>
  )
}

export default App
