import React from 'react';
import MainDashboard from './views/MainDashboard';
import Navbar from './components/NavBar';

const App = () => {
  return (
      <div>
          <Navbar />
          <MainDashboard />
      </div>
  );
}

export default App;