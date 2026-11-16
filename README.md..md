# TERRAVISION | Análise de relevo montanhoso

**Tema:** Cadeias montanhosas e relevo acentuado: sombras e modelagem 3D  
**Estudante:** Emily Reis de Camargo  
**Turma:** 3º D – Desenvolvimento de Sistemas  
**Disciplinas:** Ciências de Dados e Computação Gráfica

---

## 1. Sobre o projeto

O TERRAVISION é um projeto escolar desenvolvido em Python para estudar como dados de altitude podem ser utilizados na representação de terrenos montanhosos. A área escolhida para a visualização é a região da Serra da Prata, no litoral do Paraná, nas proximidades da Torre da Prata.

O projeto reúne duas partes: uma simulação simples de seleção de nível de detalhe de acordo com a altitude da câmera e um visualizador tridimensional que utiliza um modelo digital de elevação.

## 2. Objetivos

- Compreender como dados de elevação representam picos, encostas e áreas mais baixas.
- Preparar uma grade de altitudes para uso em uma visualização 3D.
- Observar como a representação tridimensional ajuda a perceber as formas do relevo.
- Relacionar o nível de detalhe da visualização à distância da câmera.
- Estudar a importância da iluminação e das sombras na interpretação de terrenos montanhosos.

## 3. Arquivos do projeto

| Arquivo ou pasta | Função |
|---|---|
| `script.py` | Simula a seleção de camadas de resolução com base em valores de altitude da câmera. |
| `preparar_terreno.py` | Recorta uma área do modelo digital de elevação, redimensiona os dados e salva uma matriz NumPy. |
| `app.py` | Abre a janela do TERRAVISION e desenha a matriz de elevação em 3D usando OpenGL. |
| `dados/25S495ZN.tif` | Arquivo de elevação original utilizado no processamento. |
| `dados/terreno_400.npy` | Matriz de elevação processada, com 400 linhas e 400 colunas. |
| `dados/terreno_300.npy` | Versão anterior da matriz, mantida como alternativa. |
| `imagens/` | Capturas de tela utilizadas como evidências e referências do estudo. |

## 4. Desenvolvimento em Python

### 4.1 Simulação de nível de detalhe

O arquivo `script.py` contém a função `carregar_camada_satelite(lista_altitudes)`. Ela recebe uma lista de valores de altitude da câmera e utiliza estruturas condicionais (`if`, `elif` e `else`) para classificar a visualização em três níveis:

| Altitude da câmera | Classificação simulada | Representação descrita pelo programa |
|---|---|---|
| Acima de 10.000 m | Baixa resolução | Visão geral das cadeias montanhosas |
| De 1.000 m até 10.000 m | Média resolução | Picos, vales e encostas |
| Abaixo de 1.000 m | Alta resolução | Rochas, pequenas encostas e sombras do relevo |

O programa verifica se foram informadas pelo menos cinco altitudes e percorre os valores com um laço `for`.

**Limitação:** essa parte é uma simulação didática. Ela não baixa imagens de satélite nem altera automaticamente a resolução de uma camada real.

### 4.2 Preparação dos dados de elevação

O arquivo `preparar_terreno.py` utiliza as bibliotecas Rasterio e NumPy. Ele abre o arquivo GeoTIFF `dados/25S495ZN.tif`, seleciona uma área ao redor das coordenadas aproximadas usadas para a região de estudo e redimensiona os dados para uma grade de 400 × 400 valores.

A reamostragem utiliza o método bilinear. Os valores sem dados são convertidos para `NaN`, e a matriz final é salva como `dados/terreno_400.npy`.

Na execução registrada durante o desenvolvimento, o processamento informou:

- Dimensões: 400 × 400;
- Altitude mínima da matriz processada: -0,25 m;
- Altitude máxima da matriz processada: 1.452,46 m.

Esses valores correspondem à área recortada e reamostrada pelo programa. Não devem ser interpretados como uma medição topográfica de precisão do cume.

### 4.3 Visualização tridimensional

O arquivo `app.py` carrega a matriz `dados/terreno_400.npy` e utiliza GLFW e PyOpenGL para abrir uma janela e desenhar a superfície do terreno com triângulos. As coordenadas horizontais formam a malha, enquanto os valores de elevação determinam a altura dos pontos.

O programa utiliza cores diferentes conforme a proporção da altitude dentro do intervalo da matriz: tons de verde para áreas mais baixas, marrom para valores intermediários e tons claros para áreas mais altas. A escala vertical é ajustada para tornar as diferenças de altitude mais perceptíveis.

**Limitação:** a versão atual apresenta a superfície em 3D com cores por altitude. Ela não aplica uma textura de imagem de satélite nem calcula sombras solares fisicamente. As sombras são discutidas como conceito de interpretação do relevo, mas não são simuladas por um sistema de iluminação avançado nesta versão.

## 5. Sombras, relevo e modelagem 3D

Em terrenos montanhosos, a iluminação influencia a maneira como percebemos as encostas e os vales. Regiões voltadas para a fonte de luz tendem a parecer mais iluminadas, enquanto outras podem ficar mais escuras. Esse contraste pode ajudar a interpretar a inclinação e a profundidade do relevo.

A modelagem 3D utiliza os valores de elevação para construir uma superfície com variações de altura. Assim, picos, encostas e áreas mais baixas podem ser observados em uma perspectiva tridimensional.

No TERRAVISION, a altura dos vértices é obtida a partir da matriz de elevação. A visualização é uma representação computacional do terreno, e não uma reprodução fotográfica do local.

## 6. Relação com a interface do Google Earth e Gestalt

O Google Earth permite explorar diferentes regiões por meio de pesquisa, aproximação e afastamento da câmera e visualizações do terreno. A mudança de escala ajuda o usuário a observar primeiro o contexto geográfico e depois detalhes locais.

Dois princípios da Gestalt que podem ser relacionados à interface são:

### 6.1 Figura-fundo

A área do mapa ou do terreno funciona como foco principal da tela, enquanto menus e controles aparecem separados visualmente. Essa distinção ajuda o usuário a concentrar a atenção na região explorada.

### 6.2 Proximidade

Ferramentas relacionadas aparecem agrupadas, e informações de um local são apresentadas próximas umas das outras. Essa organização facilita encontrar controles e compreender quais elementos pertencem ao mesmo conjunto.

## 7. Como executar

Os comandos abaixo devem ser executados no terminal, dentro da pasta principal do projeto.

Instale as bibliotecas necessárias:

```bash
python -m pip install numpy rasterio glfw PyOpenGL
```

Para gerar novamente a matriz de elevação:

```bash
python preparar_terreno.py
```

Para abrir o visualizador 3D:

```bash
python app.py
```

Para executar a simulação de nível de detalhe:

```bash
python script.py
```

O visualizador depende dos arquivos existentes na pasta `dados`. O arquivo `dados/25S495ZN.tif` é necessário para executar novamente o processamento; para abrir diretamente o visualizador, é necessário que `dados/terreno_400.npy` esteja presente.

## 8. Evidências

As capturas de tela de referência estão organizadas na pasta `imagens/` do projeto.

## 9. Conclusão

O desenvolvimento do TERRAVISION permitiu trabalhar com dados de elevação, preparar uma matriz numérica e utilizar essa matriz para construir uma visualização tridimensional de um terreno montanhoso. Também foi possível relacionar a escala de observação, a representação do relevo, as cores e a importância da iluminação e das sombras na leitura de paisagens.

O projeto possui limitações: a seleção de resolução em `script.py` é uma simulação, e o visualizador atual não realiza texturização por imagens de satélite nem cálculo físico de sombras. Mesmo assim, a atividade demonstra uma aplicação prática de Python, processamento de dados geográficos e computação gráfica.

## 10. Referências

- TOPODATA / Instituto Nacional de Pesquisas Espaciais (INPE): dados de elevação utilizados como base para o modelo digital do terreno.
- Google Earth: https://earth.google.com/web/
- Instituto Água e Terra do Paraná (IAT): https://www.iat.pr.gov.br/
