
import rasterio
import numpy as np
from rasterio.windows import from_bounds
from rasterio.enums import Resampling

# Localização aproximada da Torre da Prata
longitude = -48.6885
latitude = -25.6271

# Arquivo de elevação
arquivo = "dados/25S495ZN.tif"

# Abrir o modelo digital de elevação
with rasterio.open(arquivo) as terreno:

    # Definir uma área ao redor do cume
    janela = from_bounds(
        longitude - 0.20,
        latitude - 0.20,
        longitude + 0.20,
        latitude + 0.20,
        terreno.transform
    )

    # Preparar uma grade de 400 x 400
    elevacao = terreno.read(
        1,
        window=janela,
        out_shape=(400, 400),
        masked=True,
        resampling=Resampling.bilinear
    )

# Converter os dados para números decimais
elevacao = np.ma.filled(elevacao, np.nan).astype(np.float32)

# Salvar a malha preparada
np.save("dados/terreno_400.npy", elevacao)

print("Terreno preparado com sucesso!")
print("Dimensões:", elevacao.shape)
print("Altitude mínima:", round(float(np.nanmin(elevacao)), 2), "m")
print("Altitude máxima:", round(float(np.nanmax(elevacao)), 2), "m")
