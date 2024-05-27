import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainDashboard from './views/MainDashboard';
import Navbar from './components/NavBar';
import AboutPage from './views/AboutPage';

const App = () => {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<MainDashboard />} />
          <Route path="/sobre" element={<AboutPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;