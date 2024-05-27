import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';
import api from '../../api';

const StatesBarOverview = () => {
  const [estadosList, setEstadosList] = useState([]);
  const [quantidadeMunicipiosList, setQuantidadeMunicipiosList] = useState([]);
  const [populacaoList, setPopulacaoList] = useState([]);
  const [pibList, setPibList] = useState([]);
  const [rendaMensalList, setRendaMensalList] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get('/estados/');
        const data = response.data;
        
        const estados = data.map(estado => estado.sigla);
        const quantidadeMunicipios = data.map(estado => estado.quantidade_municipios);
        const populacao = data.map(estado => estado.populacao);
        const pib = data.map(estado => estado.pib);
        const rendaMensal = data.map(estado => estado.rendimento_mensal);

        setEstadosList(estados);
        setQuantidadeMunicipiosList(quantidadeMunicipios);
        setPopulacaoList(populacao);
        setPibList(pib);
        setRendaMensalList(rendaMensal);
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    };

    fetchData();
  }, []);

  const data = [
    {
      x: estadosList,
      y: quantidadeMunicipiosList,
      type: 'bar',
      name: 'Quantidade de Municípios'
    },
    {
      x: estadosList,
      y: populacaoList,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'População',
      hovertemplate: '%{x}: %{y} (este valor multiplicado por 100.000)'
    },
    {
      x: estadosList,
      y: pibList,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'PIB',
      hovertemplate: '%{x}: %{y} (este valor multiplicado por 1.0000.000)'
    },
    {
      x: estadosList,
      y: rendaMensalList,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Rendimento Mensal per capita',
      hovertemplate: '%{x}: %{y} (este valor multiplicado por 10)'
    }
  ];

  return (
    <Plot
      data={data}
      layout={{
        title: 'Informações por Estado',
        titlefont: { color: '#114784', size: 25 },
        legend: { font: { color: '#114784', size: 14 } },
        xaxis: { title: 'Estados' },
        yaxis: { title: 'Valores' },
      }}
      config={{ displaylogo: false }}
      useResizeHandler={true}
      style={{ width: "100%", height: "100%" }}
    />
  );
}

export default StatesBarOverview;
