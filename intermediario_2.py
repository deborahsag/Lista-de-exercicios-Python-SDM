class LuminariaSmart:
    def __init__(self, id):
        self.id = id
        self.ligada = False
        self.intensidade = 0

    def liga_desliga(self):
        if (self.ligada == False):
            self.ligada = True
        else:
            self.ligada = False

    def ajuste_intensidade(self, nova_intensidade):
        if (nova_intensidade >= 0 and nova_intensidade <= 100):
            self.intensidade = nova_intensidade
        else:
            print("Erro: intensidade inválida.")
    
    def relatorio(self):
        if (self.ligada):
            print(f"A luminária está ligada e sua intensidade é {self.intensidade}%.")
        else:
            print('A luminária está desligada.')

def main():
    luminaria = LuminariaSmart(1)
    luminaria.liga_desliga()
    luminaria.ajuste_intensidade(75)
    luminaria.relatorio()

if __name__ == "__main__":
    main()
