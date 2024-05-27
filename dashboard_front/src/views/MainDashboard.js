import React, { useState } from "react";
import "./MainDashboard.css";
import BrazilMap from "../components/BrazilMap";
import StateDetail from "../components/StateDetail";
import StatesBarOverview from "../components/graphs/OverviewGraph";

const MainDashboard = () => {
  const [estadoSelecionado, setEstadoSelecionado] = useState(null);

  const handleEstadoClick = (estado) => {
    setEstadoSelecionado(estado);
  };

  return (
    <div className="main-dashboard-container">
      <div className="map-detail-container">
        <div className="states-map">
          <BrazilMap onEstadoClick={handleEstadoClick} />
        </div>
        <div className="states-detail">
          {estadoSelecionado ? (
            <StateDetail estadoSigla={estadoSelecionado} />
          ) : (
            <div className="label-select-state">Selecione um estado no mapa ao lado para ver mais detalhes</div>
          )}
        </div>
      </div>
      <div className="states-overview-container">
        <StatesBarOverview />
      </div>
    </div>
  );
};

export default MainDashboard;