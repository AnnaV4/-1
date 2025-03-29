// src/App.tsx
import React from 'react'
import MeetingForm from './components/MeetingForm'
import MeetingsList from './components/MeetingsList'

const App = () => {
  return (
    <>
      <h1>Планировщик собраний</h1>
      <MeetingForm />
      <hr />
      <MeetingsList />
    </>
  )
}

export default App