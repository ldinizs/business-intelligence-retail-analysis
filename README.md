# 📊 Business Intelligence: Retail Analysis Project

Este projeto de **BI** foi desenvolvido para analisar o desempenho estratégico de uma operação de varejo entre os anos de **2014 e 2017**. O foco é transformar dados brutos em inteligência acionável, monitorando KPIs de vendas e lucratividade.

---

## 🛠️ Stack Tecnológica
* 🖼️ **Tableau Public**: Plataforma utilizada para a criação de todos os dashboards interativos e visualizações de dados.
* 🐍 **Python**: Manipulação e tratamento da base de dados.
* 📁 **Git/GitHub**: Controle de versão e documentação do projeto.
* 💾 **Dataset Original**: [Fonte de dados pública (Kaggle)](https://www.kaggle.com/datasets/abrahamkevan/supermarket-sales).
  
---

## 📑 Estrutura das Entregas
O projeto é composto por 4 etapas analíticas complementares:

* ✔️ **Entrega 1**: Tendências de Vendas, Lucro e Sazonalidade.
* ⏳ **Entrega 2**: Rentabilidade por Categoria e Subcategoria.
* ⏳ **Entrega 3**: Rentabilidade Geográfica (Mapa de Calor por Estado).
* ⏳ **Entrega 4**: Market Share e Regionalidade.

---

## 🔍 Detalhamento: Entrega 1
### *Tendências de Vendas, Lucro e Sazonalidade*

<img width="1821" height="814" alt="image" src="https://github.com/user-attachments/assets/e935c532-9204-466f-bf5f-a657e25d9f3e" />


Esta análise foca no comportamento temporal do negócio, correlacionando o crescimento do volume de vendas com a variação real do lucro líquido.

#### 📈 Análise dos Dados
* 📅 **Sazonalidade (T4)**: Identifica-se um padrão de pico no quarto trimestre de cada ano, com o faturamento recorde de **R$ 280K** no T4 de 2017.
* 📉 **Descompasso Vendas vs. Lucro**: No T3 de 2016, as vendas cresceram **5,66%**, mas o lucro caiu **-3,46%**, indicando uma redução de margem nesse período.
* 🚀 **Recuperação de Performance**: O T4 de 2016 foi o período de maior eficiência na variação de lucro, registrando uma alta de **141,03%**.
* 📊 **Volume Anual**: Nota-se uma tendência de crescimento sustentado, com as vendas subindo de R$ 180K (final de 2014) para R$ 280K (final de 2017).

💡 **Insight Estratégico**
> O dashboard possibilita identificar períodos de maior crescimento e momentos de retração na lucratividade. Ele apoia a tomada de decisão estratégica ao indicar quando o negócio performa melhor e onde ajustes são necessários para garantir que o aumento de vendas resulte em ganho real de lucro.
* 🚀 **Dashboard Interativo**: [Visualize no Tableau Public](https://public.tableau.com/views/DASHBOARDBUSINESSANALYSIS/SalesandProfitTrends?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
* 🎥 Vídeo de apresentação: [Clique aqui](https://www.canva.com/design/DAHDT8U-iJo/eBben5biyoPC-WH-2jCrRg/watch?utm_content=DAHDT8U-iJo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h4c00c9330f)
---
## 🔍 Detalhamento: Entrega 2
### *Rentabilidade por Categoria e Subcategoria*

<img width="1707" height="678" alt="image" src="https://github.com/user-attachments/assets/fef71cae-93a8-44e9-b520-2632b18bd213" />


Esta visão detalha a performance financeira do mix de produtos, permitindo identificar quais itens sustentam a margem do negócio e quais geram prejuízo operacional.

#### 📈 Análise dos Dados
* 🏆 **Subcategoria Estrela (Copiers)**: As Copiadoras demonstram lucratividade excepcional, atingindo o pico de **R$ 25.031,79** de lucro no ano de 2017.
* 📈 **Consistência em Phones e Accessories**: Mantêm lucros sólidos ano após ano, com os Telefones gerando **R$ 12.849,33** em 2017, consolidando-se como itens essenciais para o fluxo de caixa.
* ⚠️ **Ponto Crítico (Tables)**: A subcategoria de Mesas (Tables) apresenta um gargalo financeiro constante, encerrando 2017 com prejuízo de **-R$ 8.140,69**.
* 📉 **Oscilações em Machines**: Apresenta alta volatilidade, registrando lucro negativo em 2017 (**-R$ 2.869,22**), o que exige revisão na estratégia de fornecedores.

💡 **Insight Estratégico**
> Este dashboard identifica quais produtos trazem retorno e quais "corroem" a margem. O insight aponta para a necessidade urgente de reposicionar ou descontinuar a linha de **Tables** (Mesas), enquanto o investimento deve ser priorizado para **Copiers** (Copiadoras), devido à sua alta eficiência.
* 🚀 **Dashboard Interativo**: [Visualize no Tableau Public](https://public.tableau.com/views/DASHBOARDBUSINESSANALYSIS2/ProfitabillybyCategory?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
* 🎥 Vídeo de apresentação: [Clique aqui](https://canva.link/42h2u05am68b1e6)
---

## 🔍 Detalhamento: Entrega 3
### *Rentabilidade Geográfica (Mapa de Calor)*

<img width="1851" height="753" alt="image" src="https://github.com/user-attachments/assets/9f4999bc-b48b-44c5-a824-af46513a5879" />

Mapeamento de desempenho por estado para identificação de áreas deficitárias e oportunidades regionais.

#### 📈 Análise dos Dados
* 🗺️ **Zonas de Prejuízo**: Estados como **Texas (-15,12%)**, **Illinois (-15,73%)**, **Pennsylvania (-21,69%)** e **Ohio (-17,42%)** operam com margens negativas preocupantes.
* 🟢 **Destaques Positivos**: Estados como **New York (35,77%)** e **Washington (32,80%)** sustentam as melhores margens de lucro.
* 💰 **Volume Regional**: A região **East** atingiu o maior faturamento anual em 2017, somando **R$ 213,1K**.

💡 **Insight Estratégico**
> O mapa revela problemas estruturais em estados específicos do Sul e Centro-Oeste. A estratégia deve focar na revisão de custos logísticos ou tributários nestas áreas para reverter o cenário de prejuízo.
* 🚀 **Dashboard Interativo**: [Visualize no Tableau Public](https://public.tableau.com/views/DASHBOARDBUSINESSANALYSIS3/DASH3?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
* 🎥 Vídeo de apresentação: [Clique aqui](https://canva.link/hyu9i2b1q02x3p5)
---
