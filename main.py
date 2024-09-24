import threading
import random

def buscar_maior(lista, inicio, fim, resultado, indice):
    maior_valor = lista[inicio]
    for i in range(inicio + 1, fim):
        if lista[i] > maior_valor:
            maior_valor = lista[i]
    resultado[indice] = maior_valor

def main():
    tamanho_lista = 100
    lista = [random.randint(1, 1000) for _ in range(tamanho_lista)]
    print(f"Lista: {lista}")

    resultado = [None, None]
    meio_lista = tamanho_lista // 2

    tarefa1 = threading.Thread(target=buscar_maior, args=(lista, 0, meio_lista, resultado, 0))
    tarefa2 = threading.Thread(target=buscar_maior, args=(lista, meio_lista, tamanho_lista, resultado, 1))

    tarefa1.start()
    tarefa2.start()

    tarefa1.join()
    tarefa2.join()

    maior_encontrado = max(resultado)
    print(f"O maior valor encontrado foi: {maior_encontrado}")

if __name__ == "__main__":
    main()
