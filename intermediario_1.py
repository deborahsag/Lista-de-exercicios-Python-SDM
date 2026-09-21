import numpy as np

def analisar_temperaturas_np(lista_temperaturas):
    l_t = np.array(lista_temperaturas)
    temperatura_media = np.mean(l_t)
    ultrapassou_30 = sum(l_t > 30.0)
    return temperatura_media, ultrapassou_30

def analisar_temperaturas(lista_temperaturas):
    temperatura_media = sum(lista_temperaturas)/len(lista_temperaturas)
    ultrapassou_30 = sum(temperatura > 30.0 for temperatura in lista_temperaturas)
    return temperatura_media, ultrapassou_30

def main():
    temperaturas = [22.5, 25.0, 31.2, 28.4, 19.8]
    
    print('Com numpy:')
    
    tm, u30 = analisar_temperaturas_np(temperaturas)
    
    print(f"Temperatura média: {tm:.2f}")
    print(f"Dias com temperatura acima de 30.0: {u30}")

    print('\nSem numpy:')

    tm, u30 = analisar_temperaturas(temperaturas)
    
    print(f"Temperatura média: {tm:.2f}")
    print(f"Dias com temperatura acima de 30.0: {u30}")


if __name__ == "__main__":
    main()
