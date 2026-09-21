class DispositivoIoT:
    def __init__(self, nome, bateria):
        self.nome = nome
        
        if (bateria >=0 and bateria <= 100):
            self.bateria = bateria
        else:
            print("Erro: o nível de bateria deve estar entre 0 e 100.")


class HubCentral:
    def __init__(self):
        self.dispositivos_conectados = []

    def adicionar_dispositivo(self, dispositivo):
        self.dispositivos_conectados.append(dispositivo)

    def relatorio_bateria_baixa(self):
        bateria_baixa = False
        relatorio = "Dispositivos com bateria abaixo de 20%:"
        
        for dispositivo in self.dispositivos_conectados:
            if (dispositivo.bateria < 20):
                bateria_baixa = True
                relatorio += f" {dispositivo.nome}"
        
        if (bateria_baixa):
            print(relatorio)
        else:
            print("Nenhum dispositivo com bateria abaixo de 20%.")


def main():
    print("Teste da criação de dispositivos:")
    dispositivo_0 = DispositivoIoT("Teste", -1)
    dispositivo_00 = DispositivoIoT("Teste", 190)

    print("\nHub 1:")
    dispositivo_1 = DispositivoIoT("Alexa", 100)
    dispositivo_2 = DispositivoIoT("Tablet", 100)
    dispositivo_3 = DispositivoIoT("Celular", 100)

    hub_1 = HubCentral()
    hub_1.adicionar_dispositivo(dispositivo_1)
    hub_1.adicionar_dispositivo(dispositivo_2)
    hub_1.adicionar_dispositivo(dispositivo_3)

    hub_1.relatorio_bateria_baixa()

    print("\nHub 2:")
    dispositivo_4 = DispositivoIoT("Alexa", 10)
    dispositivo_5 = DispositivoIoT("Tablet", 19)
    dispositivo_6 = DispositivoIoT("Celular", 100)

    hub_2 = HubCentral()
    hub_2.adicionar_dispositivo(dispositivo_4)
    hub_2.adicionar_dispositivo(dispositivo_5)
    hub_2.adicionar_dispositivo(dispositivo_6)
    
    hub_2.relatorio_bateria_baixa()


if __name__ == "__main__":
    main()
