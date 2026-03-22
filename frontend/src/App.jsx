import React from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Feed from './pages/Feed'
import { isAuthenticated } from './utils/auth'

function PrivateRoute({ children }) {
  return isAuthenticated() ? children : <Navigate to="/login" />
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/feed" element={<PrivateRoute><Feed /></PrivateRoute>} />
        <Route path="/" element={<Navigate to="/feed" />} />
      </Routes>
    </Router>
  )
}

export default App
