
def carregar_camada_satelite(lista_altitudes):

    # Verifica se existem pelo menos 5 altitudes
    if len(lista_altitudes) < 5:
        print("Erro: informe pelo menos 5 altitudes.")
        return

    # Percorre cada altitude informada
    for altitude in lista_altitudes:

        print("\n------------------------------")
        print(f"Altitude da camera: {altitude} metros")

        # Baixa resolução
        if altitude > 10000:
            print("Camada: BAIXA RESOLUCAO")
            print("Renderizando visao geral das cadeias montanhosas.")

        # Média resolução
        elif altitude >= 1000:
            print("Camada: MEDIA RESOLUCAO")
            print("Renderizando picos, vales e encostas.")

        # Alta resolução
        else:
            print("Camada: ALTA RESOLUCAO")
            print("Renderizando rochas, pequenas encostas e sombras do relevo.")

# Lista com cinco altitudes para teste
altitudes = [25000, 15000, 8000, 3500, 500]

# Executa a funcao
carregar_camada_satelite(altitudes)
