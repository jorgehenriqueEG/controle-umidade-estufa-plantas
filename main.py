def verificar_umidade(lista_umidades):
    alertas = []
    umidade_minima = 40
    for i in range(len(lista_umidades)):
        if lista_umidades[i] < umidade_minima:
            alertas.append(f"Alerta: Sensor {i+1} com umidade {lista_umidades[i]}%")
    if not alertas:
        return "Nenhum alerta. Umidade está adequada."
    return "\n".join(alertas)

if __name__ == "__main__":
    leituras = [45, 38, 52, 35]
    resultado = verificar_umidade(leituras)
    print(resultado)