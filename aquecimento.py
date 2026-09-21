def main():
    porta_destravada = False
    nivel_acesso = int(input('Informe seu nível de acesso: '))

    if (nivel_acesso >= 5):
        porta_destravada = True
        print('Acesso liberado')
    else:
        print('Acesso negado: Permissão insuficiente')

if __name__ == "__main__":
    main()
    