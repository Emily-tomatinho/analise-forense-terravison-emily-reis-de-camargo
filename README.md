# TERRAVISION | Explorador geográfico da Serra da Prata

Aplicativo desktop em Python, com janela própria. Ele não abre o Google Chrome.

## Como abrir no Windows sem usar arquivo BAT

1. Extraia a pasta `TERRAVISION` inteira para um local fácil de encontrar, como Downloads.
2. Abra a pasta `TERRAVISION` no Explorador de Arquivos.
3. Clique na barra de endereço da pasta, digite `powershell` e pressione Enter.
4. Na janela azul do PowerShell, digite o comando abaixo e pressione Enter:

   ```powershell
   python -m pip install -r requirements.txt
   ```

   Esse comando instala as bibliotecas necessárias (PySide6 e NumPy). Na primeira vez, precisa de internet.

5. Quando a instalação terminar, digite:

   ```powershell
   python app.py
   ```

   Esse comando abre o TERRAVISION em uma janela própria.

**Importante:** este pacote não contém instalador `.exe` nem arquivo `.bat`. Não é necessário desativar o Controle de Aplicativo Inteligente do Windows. Se o Windows ou o Python mostrar um erro, pare e copie a mensagem para receber ajuda. Não altere as configurações de segurança do notebook.

## Recursos
- Visualização 2D com imagem de satélite (Esri).
- Modo de relevo sombreado (OpenTopoMap) e mapa combinado com hillshade.
- Modo 3D com malha de elevação local derivada da matriz TOPODATA/INPE que acompanha o projeto.
- Botões de zoom + e -, retorno ao enquadramento inicial, indicador de altitude e controles de iluminação/malha/vista.
- Navegação 2D por arraste e 3D por arraste do mouse e roda.

## Controles
- `+` / `-`: aproximar e afastar.
- Arrastar no mapa 2D: mover a região.
- Arrastar no modo 3D: orbitar o terreno.
- Roda do mouse no 3D: aproximar/afastar.
- Painel esquerdo: Satélite 2D, Terreno 3D, Relevo sombreado, Mapa + relevo, iluminação, malha, vista superior e inclinada.

## Dados, escala e limitações
- Centro aproximado: Torre da Prata, latitude -25.6271, longitude -48.6885.
- O mapa 2D usa serviços de mapas online e depende de internet. As atribuições dos provedores aparecem na interface.
- O modo 3D usa uma matriz de elevação local recortada do arquivo TOPODATA processado que acompanha o projeto. Não é um modelo fotogramétrico nem uma textura de satélite 3D.
- A extensão de 4,92 km é uma referência de enquadramento geográfico, não um círculo ou uma linha desenhada no mapa. O recorte do modelo de elevação foi preparado para abranger aproximadamente 4,9 km para cada lado do centro.
- O indicador de 1.000 a 10.000 m é uma escala didática aproximada de visualização, não uma medição GPS/barométrica nem uma escala cartográfica rigorosa.
- A visualização 3D é um modelo digital de elevação colorido. Não é uma cópia integral do Google Earth e não possui imagens oblíquas reais de satélite.

## Estrutura
- `app.py`: janela desktop Python.
- `interface.html`: interface de mapas 2D e cena 3D.
- `dados/terreno_recorte.json`: grade de elevação usada no 3D.
- `dados/terreno_400.npy`: matriz original processada.
- `preparar_terreno.py`: rotina anterior de preparação do DEM (requer GeoTIFF original).

## Fonte de elevação
TOPODATA / INPE: https://www.dsr.inpe.br/topodata/


Correção de carregamento: os dados locais de elevação são incorporados à interface pelo aplicativo Python, evitando falha ao buscar o JSON por caminho relativo.
