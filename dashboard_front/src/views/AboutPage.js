import React from 'react';
import './AboutPage.css';
const AboutPage = () => {
  return (
    <div className="sobre-container">
      <h2 className="sobre-heading">Sobre</h2>
      <div className="sobre-content">
        <p>
          Este dashboard tem o intuito de ser um projeto sem compromisso financeiro, apenas um projeto de demonstração para um exercício proposto.
        </p>
        <p>
          O projeto está disponível no <a href="https://github.com/leemonades/dashboard_ibge" target="_blank" rel="noopener noreferrer">GitHub</a>.
        </p>
        <p>
          Os dados foram adquiridos diretamente da <a href="https://servicodados.ibge.gov.br/api/docs/localidades" target="_blank" rel="noopener noreferrer">API do IBGE</a>.
        </p>
        <p>
          Importante ressaltar que há espaço para muitas melhorias mas não foi possível devido ao tempo proposta no exercício.
        </p>
        <p>
          As stacks utilizadas neste projeto foram:
        </p>
        <ul>
          <li>React</li>
          <li>Django/Python</li>
          <li>PostgreSQL</li>
        </ul>
        <p>
          Fico à disposição para dúvidas, comentários, sugestões e contribuições.
        </p>
      </div>
    </div>
  );
}

export default AboutPage;