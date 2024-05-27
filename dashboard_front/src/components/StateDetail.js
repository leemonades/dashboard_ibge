import React, { useEffect, useState } from "react";
import "./StateDetail.css";
import api from "../api";
import {
  FaFlag,
  FaIdBadge,
  FaCity,
  FaUsers,
  FaMoneyBillWave,
  FaChartLine,
} from "react-icons/fa";

const Spinner = () => {
  return (
    <div className="spinner-container">
      <div className="spinner"></div>
    </div>
  );
};

const StateDetail = ({ estadoSigla }) => {
  const [estadoData, setEstadoData] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);

      try {
        const response = await api.get(`/estado/${estadoSigla}/`);
        const data = response.data;
        setEstadoData(data);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching state data:", error);
      }
    };

    fetchData();
  }, [estadoSigla]);

  if (loading) {
    return <Spinner />;
  }

  if (!estadoData) return null;

  return (
    <div className="state-detail-container">
      <h1>{estadoData.nome}</h1>
      <div className="state-details">
        <DetailItem icon={<FaFlag />} label="Sigla" value={estadoData.sigla} />
        <DetailItem
          icon={<FaIdBadge />}
          label="ID IBGE"
          value={estadoData.id}
        />
        <DetailItem
          icon={<FaCity />}
          label="Quantidade de Municípios(2024)"
          value={estadoData.quantidade_municipios}
        />
        <DetailItem
          icon={<FaUsers />}
          label="População(2021)"
          value={estadoData.populacao}
        />
        <DetailItem
          icon={<FaChartLine />}
          label="PIB(2021)"
          value={estadoData.pib}
        />
        <DetailItem
          icon={<FaMoneyBillWave />}
          label="Rendimento Médio Mensal per capita(2023)"
          value={estadoData.rendimento_mensal}
        />
      </div>
    </div>
  );
};

const DetailItem = ({ icon, label, value }) => (
  <div className="detail-item">
    <div className="detail-content">
      <div className="detail-icon">{icon}</div>
      <div className="detail-label">{label}:</div>
    </div>
    <div className="detail-value">{value}</div>
  </div>
);

export default StateDetail;