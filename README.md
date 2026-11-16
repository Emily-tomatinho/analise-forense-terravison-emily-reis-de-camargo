# Cadeias Montanhosas e Relevo Acentuado – Sombra e Modelagem 3D
# Relatório Técnico de Análise Forense e Computação Gráfica

**COLÉGIO ESTADUAL RODOLPHO ZANINELLI**  
**Curso:** Ensino Médio Técnico em Desenvolvimento de Sistemas  
**Turma:** 3º D – Matutino  
**Estudante:** Emily Reis de Camargo  
**Professora:** Angélica Neckel  
**Disciplinas:** Ciências de Dados e Computação Gráfica  

---

## 1. APRESENTAÇÃO DO PROJETO

O TERRAVISION é um projeto desenvolvido em Python com o objetivo de estudar a representação digital de terrenos montanhosos, utilizando dados de elevação e recursos de computação gráfica.

A área escolhida para o estudo está localizada na região da Serra da Prata, no litoral do Paraná, nas proximidades da Torre da Prata.

O trabalho busca demonstrar como informações geográficas podem ser processadas e transformadas em representações visuais, permitindo observar características como picos, encostas, vales e diferenças de altitude.

A proposta também estabelece uma relação com sistemas de visualização geográfica, como o Google Earth, considerando aspectos de organização de dados, níveis de detalhe, navegação e representação tridimensional.

## 2. OBJETIVOS

### 2.1 Objetivo geral

Analisar como dados de elevação podem ser utilizados para representar cadeias montanhosas e terrenos de relevo acentuado por meio de processamento de dados e modelagem tridimensional.

### 2.2 Objetivos específicos

- Compreender a organização de dados geográficos em matrizes.
- Aplicar estruturas condicionais e de repetição em Python.
- Estudar o conceito de Level of Detail (LoD).
- Utilizar dados de altitude na construção de uma superfície tridimensional.
- Analisar a influência das cores, da iluminação e das sombras na interpretação do relevo.
- Relacionar princípios de design e leis da Gestalt à interface de visualização.

## 3. DESENVOLVIMENTO E ORGANIZAÇÃO DOS DADOS

### 3.1 Seleção do nível de detalhe (LoD)

Em aplicações de visualização geográfica, a quantidade de detalhes exibidos pode variar conforme a distância ou altitude da câmera virtual.

Esse processo é conhecido como Level of Detail (LoD). Seu objetivo é evitar o processamento desnecessário de informações quando o usuário observa uma área muito extensa.

No arquivo `script.py`, a função `carregar_camada_satelite(lista_altitudes)` utiliza estruturas condicionais para classificar a visualização de acordo com a altitude informada.

| Altitude da câmera | Nível de detalhe | Elementos relacionados ao tema |
|---|---|---|
| Acima de 10.000 m | Baixa resolução | Visão geral das cadeias montanhosas |
| Entre 1.000 m e 10.000 m | Média resolução | Picos, vales e encostas |
| Abaixo de 1.000 m | Alta resolução | Detalhes do relevo e pequenas variações da superfície |

A função utiliza `if`, `elif` e `else` para verificar as condições e um laço `for` para percorrer os valores de altitude.

Essa implementação representa uma simulação didática da seleção de níveis de detalhe.

### 3.2 Preparação dos dados de elevação

Os dados de elevação são utilizados para representar as diferenças de altura existentes no terreno.

O processamento descrito no projeto utiliza Python, NumPy e Rasterio para trabalhar com um arquivo geográfico no formato GeoTIFF.

A partir dos dados originais, é possível selecionar uma área de interesse, realizar a reamostragem e organizar as altitudes em uma matriz numérica.

Durante o processamento registrado, foram obtidos os seguintes resultados:

| Característica | Resultado |
|---|---|
| Dimensões da matriz principal | 400 × 400 |
| Tipo dos valores | float32 |
| Altitude mínima registrada | Aproximadamente -0,25 m |
| Altitude máxima registrada | Aproximadamente 1.452,46 m |

Esses valores representam os dados da matriz processada e não devem ser interpretados como uma medição topográfica de precisão do ponto mais alto da região.

### 3.3 Modelagem tridimensional

Na representação tridimensional, os valores de altitude determinam a altura dos pontos que formam a superfície do terreno.

A matriz de elevação funciona como base para a construção de uma malha, na qual as coordenadas horizontais representam a posição dos pontos e os valores numéricos determinam suas alturas.

Essa organização permite visualizar diferenças entre áreas elevadas e regiões mais baixas, facilitando a interpretação de montanhas, encostas e vales.

## 4. ETAPA 2 – COMPUTAÇÃO GRÁFICA E UX/UI

### 4.1 Processamento e tratamento de imagem

A representação de cadeias montanhosas apresenta desafios específicos para os sistemas de visualização geográfica.

Um dos principais problemas é a uniformização das imagens. Fotografias de diferentes áreas podem apresentar variações de iluminação, contraste e tonalidade. Quando essas imagens são combinadas, as diferenças podem ficar perceptíveis na transição entre uma região e outra.

Outro desafio está relacionado às sombras produzidas pelo relevo. Montanhas elevadas podem bloquear a iluminação em determinadas áreas, criando regiões mais escuras. Embora essas sombras contribuam para a percepção de profundidade, também podem dificultar a identificação de detalhes quando há pouco contraste.

A textura também precisa acompanhar a geometria do terreno. Em uma representação tridimensional, a imagem aplicada à superfície deve respeitar as diferenças de inclinação e altura para evitar distorções visuais.

No caso do TERRAVISION, os dados de elevação são utilizados para construir a superfície tridimensional. A representação por cores auxilia na diferenciação das altitudes, mas não substitui uma textura real de satélite nem um cálculo físico de iluminação e sombras.

### 4.2 Leis da Gestalt

As leis da Gestalt ajudam a compreender como os elementos visuais são organizados e percebidos pelo usuário.

Neste projeto, dois princípios são especialmente relevantes:

**Figura-Fundo**

A região geográfica apresentada na tela deve ser o elemento de maior destaque. Os menus, botões e informações complementares precisam permanecer visualmente separados do terreno.

Essa organização ajuda o usuário a manter a atenção na área analisada, sem confundir os controles da interface com os elementos do mapa.

**Proximidade**

Elementos que possuem funções relacionadas devem ficar próximos uns dos outros. Por exemplo, os controles de aproximação e afastamento podem ficar agrupados, enquanto as opções de visualização e informações de altitude podem ocupar áreas próprias da interface.

Essa organização facilita a localização das ferramentas e torna a navegação mais intuitiva.

### 4.3 Organização da interface e experiência do usuário

Uma interface de visualização geográfica precisa permitir que o usuário compreenda rapidamente onde está observando e quais ferramentas pode utilizar.

A aproximação e o afastamento da câmera são importantes para alternar entre a visão geral da cadeia montanhosa e a observação de detalhes locais.

A separação entre os controles e a área de visualização também contribui para uma experiência mais organizada.

A referência utilizada para essa proposta é a navegação do Google Earth, especialmente a mudança de escala e a possibilidade de observar o terreno em diferentes perspectivas.

## 5. RELAÇÃO ENTRE SOMBRAS, ALTITUDE E RELEVO

As sombras possuem papel importante na interpretação de terrenos montanhosos.

Quando a luz atinge uma superfície irregular, as diferentes inclinações podem produzir áreas com níveis distintos de iluminação. Esse contraste ajuda a identificar elevações, depressões e mudanças na orientação das encostas.

Na modelagem tridimensional, os valores de elevação permitem representar essas diferenças de altura.

Dessa forma, a visualização do relevo não depende apenas das cores, mas também da geometria da superfície e da maneira como a iluminação é representada.

## 6. TECNOLOGIAS E FERRAMENTAS UTILIZADAS

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Linguagem principal de desenvolvimento |
| NumPy | Organização e manipulação de matrizes numéricas |
| Rasterio | Leitura e processamento de dados geográficos |
| OpenGL | Recursos de renderização gráfica |
| PySide6 | Construção da interface da aplicação |
| GitHub | Versionamento e documentação do projeto |

*Observação: a lista de bibliotecas deve ser conferida com os arquivos de dependências da versão final publicada.*

## 7. EVIDÊNCIAS VISUAIS

Nesta seção devem ser inseridas capturas de tela que demonstrem a área estudada e o desenvolvimento do projeto.

**Figura 1 – Área de estudo no Google Earth**  
Inserir uma captura de tela da região da Serra da Prata, mostrando o tema mapeado.

**Figura 2 – Visualização do terreno no TERRAVISION**  
Inserir uma captura da aplicação em funcionamento, quando disponível.

**Figura 3 – Representação tridimensional do relevo**  
Inserir uma captura do modelo 3D, quando disponível.

## 8. CONCLUSÃO

O desenvolvimento do TERRAVISION permitiu explorar a relação entre dados geográficos, programação e computação gráfica.

O estudo demonstrou como uma matriz de elevação pode ser utilizada para representar as variações de altura de um terreno e como a seleção de níveis de detalhe pode contribuir para organizar a visualização de grandes áreas geográficas.

Também foi possível compreender a importância das sombras, das cores e dos princípios da Gestalt na interpretação do relevo e na organização de uma interface.

Além da aplicação prática dos conceitos de Python, o projeto proporcionou contato com o processamento de dados geográficos e com os fundamentos da representação tridimensional.

## 9. REFERÊNCIAS

- INPE – Instituto Nacional de Pesquisas Espaciais. TOPODATA: Banco de Dados Geomorfométricos do Brasil.
- Google Earth. Disponível em: https://earth.google.com/web/
- Instituto Água e Terra do Paraná. Disponível em: https://www.iat.pr.gov.br/
- Documentação oficial do Python: https://docs.python.org/3/
- Documentação do NumPy: https://numpy.org/doc/
- Documentação do Rasterio: https://rasterio.readthedocs.io/

---

**TERRAVISION | Análise de relevo montanhoso**  
**Emily Reis de Camargo – 3º D | Desenvolvimento de Sistemas**
