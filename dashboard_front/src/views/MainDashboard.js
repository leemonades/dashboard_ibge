import React, { useState } from 'react';
import './MainDashboard.css';
import BrazilMap from '../components/BrazilMap';
import StateDetail from '../components/StateDetail';
import StatesBarOverview from '../components/graphs/OverviewGraph';

const MainDashboard = () => {
  const [estadoSelecionado, setEstadoSelecionado] = useState(null);
  const [mapPosition, setMapPosition] = useState('left');
  const [qtdMunicipiosData, setQtdMunicipiosData] = useState(null);

  const handleEstadoClick = (estado) => {
    setEstadoSelecionado(estado);
    setMapPosition('right');
  };

  return (
    <div className="main-dashboard-container">
      <div className="map-detail-container">
        <div className="states-map" style={{
          transition: 'transform 0.5s ease-in-out',
          transform: mapPosition === 'left' ? 'translateX(0)' : 'translateX(-30%)'
        }}>
          <BrazilMap onEstadoClick={handleEstadoClick} />
        </div>
        <div className="states-detail" style={{
        }}>
          {estadoSelecionado && <StateDetail estadoSigla={estadoSelecionado} />}
        </div>
      </div>
      <div className="states-overview-container" style={{border: "1px solid black"}}>
        <StatesBarOverview qtdMunicipiosData={qtdMunicipiosData} />
      </div>
    </div>
  );
};

export default MainDashboard;