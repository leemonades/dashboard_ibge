import React from 'react';
import Plot from 'react-plotly.js';

const StatesBarOverview = ({ qtdMunicipiosData }) => {
  const estados = ['SP', 'RJ', 'MG', 'RS'];
  const quantidadeMunicipios = [645, 92, 853, 497];
  const populacao = [45919049, 17366189, 21168791, 11422973];
  const pib = [2142575938, 671998028, 1056058731, 431204603];
  const rendimentoMensal = [2583.20, 2285.40, 2242.80, 2358.10];
  const proporcaoPopulacao = populacao.map((valor, index) => valor /10000[index]);
  const proporcaoPIB = pib.map((valor, index) => valor / 1000000[index]);
  const proporcaoRendimentoMensal = rendimentoMensal.map((valor, index) => valor / 10[index]);
  console.log(proporcaoPopulacao)

  const data = [
    {
        x: estados,
        y: quantidadeMunicipios,
        type: 'bar',
        name: 'Quantidade de Municípios'
    },
    {
        x: estados,
        y: proporcaoPopulacao,
        type: 'scatter',
        mode: 'lines+markers',
        name: 'População'
    },
    {
        x: estados,
        y: proporcaoPIB,
        type: 'scatter',
        mode: 'lines+markers',
        name: 'PIB'
    },
    {
        x: estados,
        y: proporcaoRendimentoMensal,
        type: 'scatter',
        mode: 'lines+markers',
        name: 'Rendimento Mensal'
    }
];

return <Plot
    data={data}
    layout={{
        title: 'Informações por Estado',
        xaxis: { title: 'Estados' },
        yaxis: { title: 'Valores' }
    }}
/>;
}

export default StatesBarOverview;