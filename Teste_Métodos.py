#Exercício Programa 2 - MAC122 - PDA
#Nome: Kauê Capellato Junqueira Parreira
#N°USP: 11297016

import time

def LeiaArq(nomearq):
    #começa com uma lista vazia
    tab = []

    #tenta abrir o arquivo, caso não consiga, retorna None
    try:
        arquivo = open(nomearq, 'r')
    except:
        return None

    #Leitura do arquivo, retirando o "\n" de cada linha
    for linha in arquivo:
        try:
            linha = linha[:len(linha)-1]
            tab.append(linha)

        except:
            print("Erro na formação da tabela.")
            return None

    arquivo.close()
    return tab   #retorna tab (lista onde cada elemento é uma string com uma linha do arquivo)



def escreve_arquivo(ordem_arq, TAB):

    try:
        arquivo = open(ordem_arq, "w")


    except:
        print("Erro ao escrever no arquivo")
        return None

    for linha in range(len(TAB)):

        data_nascimento = str(TAB[linha][2])
        data_str = data_nascimento[6:] + '/' + data_nascimento[4:6] + '/' + data_nascimento[:4]
        nova_linha = str(TAB[linha][0]) + "," + TAB[linha][1] + "," + data_str
        arquivo.write(nova_linha + "\n")

    arquivo.close()


def matriz_infos(tab):

    ''' Função que transforma a lista TAB, em que cada elemento é uma lista contendo strings: ["<identificação>, <nome>, <data de nascimento>"], em uma matriz
        em que cada elemento é uma lista da forma: [<identificação>, "<nome>", <data de nascimento>] em que os dados de identificação e data de nascimento
        foram tranformados em inteiros para facilitar a comparação.
        Para a data de nascimento ainda, foi retirado o "/" e invertida ficando no formato YYYYMMDD '''

    matriz_tab = []

    for linha in tab:
        elemento = linha.split(",")
        data_splitada = elemento[2].split("/")
        data_comparavel = data_splitada[2] + data_splitada[1] + data_splitada[0]
        matriz_tab.append([int(elemento[0]), elemento[1], int(data_comparavel)])

    return matriz_tab


def bubble(TAB, index):

    ''' Método da bolha: começa a partir do segundo elemento e compara com o anterior, se esse segundo elemento for menor, troca com o anterior.
        Faz a comparação por determinado critério (index) estabelecido pelo usuário na lista "ordem"
        Ordem: O(n²) '''

    for i in range(len(TAB)):
        j = i
        while j > 0 and TAB[j][index] < TAB[j-1][index]:
            TAB[j-1], TAB[j] = TAB[j], TAB[j-1]
            j -= 1

    #retorna a TAB classificada por determinado critério
    return TAB



def particiona_1(TAB, inicio, fim, lista):

    ''' Função que é composta de 2 ponteiros e uma direção que indica o sentido a ser seguido pelos ponteiros.
        Fará a partição da TAB, retornando o índice do elemento pivô '''

    # variáveis de direção e ponteiros a partir do início e do final da lista
    direcao = 1
    i = inicio
    j = fim

    #Lista ordem com elementos em formato inteiro
    ordem = [int(i) for i in lista]

    while i < j:

        #Primeira classificação de acordo com determinado critério (índice)
        if TAB[i][ordem[0]] > TAB[j][ordem[0]]:

            TAB[i], TAB[j] = TAB[j], TAB[i]

            #muda a direção
            direcao = - direcao

        #avaça o ponteiro i (sentido ->)
        if direcao == 1:
            i += 1

        #avança o ponteiro j (sentido <-)
        else:
            j -= 1

    return i

def Quick_Sort_1(lista, ordem):

    # Cria a pilha de sub-listas e inicia com lista completa
    Pilha = []
    Pilha.append((0, len(lista) - 1))


    # Repete até que a pilha de sub-listas esteja vazia

    while not len(Pilha) == 0:
        inicio, fim = Pilha.pop()
        # Só particiona se há mais de 1 elemento

        if fim - inicio > 0:

            k = particiona_1(lista, inicio, fim, ordem)

            # Empilhe as sub-listas resultantes
            Pilha.append((inicio, k - 1))
            Pilha.append((k + 1, fim))

    return lista


def particiona_2(TAB, inicio, fim, lista):

    k, l = inicio, fim

    #Lista ordem com elementos em formato inteiro
    ordem = [int(i) for i in lista]
    direcao = 1

    #Função que troca os elementos de uma lista TAB caso o primeiro critério seja igual.
    #Ex.: Dados 2 critérios ['1', '0'] - Com a lista previamente classificada em 1 (pre_class = True), utiliza o critério 2 (identificação) para o desempate
    #Retorna o pivô baseando-se nessa classificação

    while k < l:
        if TAB[k][ordem[0]] == TAB[l][ordem[0]] and TAB[k][ordem[1]] > TAB[l][ordem[1]]:
            TAB[k], TAB[l] = TAB[l], TAB[k]
            direcao = - direcao

        if direcao == 1:    k += 1
        else:   l -= 1

    return k


def Quick_Sort_2(lista, ordem):

    # Cria a pilha de sub-listas e inicia com lista completa
    lista_class = Quick_Sort_1(lista, ordem)

    Pilha = []
    Pilha.append((0, len(lista_class) - 1))

    # Repete até que a pilha de sub-listas esteja vazia

    while not len(Pilha) == 0:
        inicio, fim = Pilha.pop()
        # Só particiona se há mais de 1 elemento

        if fim - inicio > 0:

            #print("kdmlekc")
            k = particiona_2(lista_class, inicio, fim, ordem)

            # Empilhe as sub-listas resultantes
            Pilha.append((inicio, k - 1))
            Pilha.append((k + 1, fim))

    return lista_class


def particiona_3(TAB, inicio, fim, lista):

    m, n = inicio, fim

    #Lista ordem com elementos em formato inteiro
    ordem = [int(i) for i in lista]
    direcao = 1

    #Função que troca os elementos de uma lista TAB caso o primeiro critério seja igual.
    #Ex.: Dados 2 critérios ['1', '0'] - Com a lista previamente classificada em 1 (pre_class = True), utiliza o critério 2 (identificação) para o desempate
    #Retorna o pivô baseando-se nessa classificação

    while m < n:
        if TAB[m][ordem[0]] == TAB[n][ordem[0]] and TAB[m][ordem[1]] == TAB[n][ordem[1]] and TAB[m][ordem[2]] > TAB[n][ordem[2]]:
            TAB[m], TAB[n] = TAB[n], TAB[m]
            direcao = - direcao

        if direcao == 1:    m += 1
        else:   n -= 1

    return m

def Quick_Sort_3(lista, ordem):

    # Cria a pilha de sub-listas e inicia com lista completa
    lista_class = Quick_Sort_2(lista, ordem)


    Pilha = []
    Pilha.append((0, len(lista_class) - 1))

    # Repete até que a pilha de sub-listas esteja vazia

    while not len(Pilha) == 0:
        inicio, fim = Pilha.pop()
        # Só particiona se há mais de 1 elemento

        if fim - inicio > 0:

            #print("kdmlekc")
            k = particiona_3(lista_class, inicio, fim, ordem)

            # Empilhe as sub-listas resultantes
            Pilha.append((inicio, k - 1))
            Pilha.append((k + 1, fim))

    return lista_class


def Classifica1(TAB, ordem):

    ''' Método 1 escolhido: Bubble Sort (método de classificação da bolha) '''

    ### Método da Bolha

    if ordem[0] == '0':    ##Classifica pela identificação


        if len(ordem) == 3 and ordem[1] == '1' and ordem[2] == '2':  ##Classifica pela identificação e dentro por nome e pelo nascimento
            lista = bubble(bubble(bubble(TAB, 2), 1), 0)

        elif len(ordem) == 3 and ordem[1] == '2' and ordem[2] == '1':  ##Classifica pela identificação e dentro por nascimento e pelo nome
            lista = bubble(bubble(bubble(TAB, 1), 2), 0)

        elif len(ordem) == 2 and ordem[1] == '1':  ##Classifica pela identificação e dentro pelo nome
            lista = bubble(bubble(TAB, 1), 0)

        elif len(ordem) == 2 and ordem[1] == '2':  ##Classifica pela identificação e dentro pelo nascimento
            lista = bubble(bubble(TAB, 2), 0)

        elif len(ordem) == 1:
            #Classifica apenas pela identificação
                lista = bubble(TAB, 0)


    elif ordem[0] == '1':    ##Classifica pelo nome


        if len(ordem) == 3 and ordem[1] == '0' and ordem[2] == '2':  ##Classifica pela nome e dentro por identificação e por data de nascimento
            lista = bubble(bubble(bubble(TAB, 2), 0), 1)

        elif len(ordem) == 3 and ordem[1] == '2' and ordem[2] == '0':  ##Classifica pela nome e dentro por data de nascimento e por identificação
            lista = bubble(bubble(bubble(TAB, 0), 2), 1)

        elif len(ordem) == 2 and ordem[1] == '0':  ##Classifica pelo nome e dentro pela identificação
            lista = bubble(bubble(TAB, 0), 1)

        elif len(ordem) == 2 and ordem[1] == '2':  ##Classifica pelo nome e dentro pela data de nascimento
            lista = bubble(bubble(TAB, 2), 1)

        elif len(ordem) == 1:    ##Classifica pelo nome
            lista = bubble(TAB, 1)


    elif ordem[0] == '2':    ##Classifica pela data de nascimento


        if len(ordem) == 3  and ordem[1] == '0' and ordem[2] == '1':  ##Classifica pela data de nascimento e dentro por identificação e pelo nome
            lista = bubble(bubble(bubble(TAB, 1), 0), 2)

        elif len(ordem) == 3 and ordem[1] == '1' and ordem[2] == '0':  ##Classifica pela data de nascimento e dentro pelo nome e por identificação
            lista = bubble(bubble(bubble(TAB, 0), 1), 2)

        elif len(ordem) == 2 and ordem[1] == '0':  ##Classifica pela data de nascimento e dentro por identificação
            lista = bubble(bubble(TAB, 0), 2)

        elif len(ordem) == 2 and ordem[1] == '1':  ##Classifica pela data de nascimento e dentro pelo nome
            lista = bubble(bubble(TAB, 1), 2)

        elif len(ordem) == 1:
            #Classifica apenas pela data de nascimento
                lista = bubble(TAB, 2)


    #retorna a lista classificada de acordo com critérios de ordem
    return lista

def Classifica2(TAB, ordem):

    ''' Método 2 escolhido: Quick Sort (método de classificação quick) '''

    ### Método QuickSort


    if len(ordem) == 3:  ##Classifica pela identificação e dentro por nome e pelo nascimento ou pela identificação e dentro por nascimento e pelo nome
        lista = Quick_Sort_3(TAB, ordem)

    elif len(ordem) == 2:  ##Classifica pela identificação e dentro pelo nome ou pela identificação e dentro pelo nascimento
        lista = Quick_Sort_2(TAB, ordem)

    else:
        #Classifica apenas pela identificação
        lista = Quick_Sort_1(TAB, ordem)


    #retorna a lista classificada de acordo com critérios de ordem
    return lista


def verifica_entrada():

    ''' Função que verifica a entrada do usuário, aceitando no mínimo 1 elemento e no máximo 3 elementos, sendo eles: 0, 1 ou 2 '''

    while True:

        try:
            string = input("Ordem de classificação: ")
            l = string.lower()

            # Se for digitado 'fim', o programa acaba
            if l == 'fim':
                return None
                break

            # Caso contrário, verifica e faz consistências
            else:
                entrada_splitada = l.split(",")

                # Verifica o tamaho da entrada (lista), valor que deve estar entre 1 e 3 (1 <= tamanho <= 3)
                if len(entrada_splitada) > 3 or len(entrada_splitada) < 1:
                    print("\nEntrada inválida. Digite novamente.\n")
                    continue

                # Verifica elemento a elemento da lista com elementos da entrada splitados
                for elemento in range(len(entrada_splitada)):
                    if entrada_splitada[elemento] not in ['0', '1', '2']:
                        raise Exception

                # Verifica se tem elementos repetidos, se encontrar, a entrada é inválida
                    elif entrada_splitada[elemento] in entrada_splitada[elemento + 1:]:
                        raise Exception

        # Se achou alguma exceção, pede para o usuário digitar novamente
        except Exception:
            print('\nEntrada inválida. Digite novamente.\n')
            continue


        else:

            # Nesse ponto a lista (entrada) está correta, apenas a retorna
            return entrada_splitada
            break


def main():
    while True:

        ordem = []

        #Pedir o nome do arquivo de origem (‘fim’: break)
        #Pedir o nome do arquivo de destino
        try:

            nomearq = input("Arquivo de origem: ")
            print()

            if nomearq.lower() == 'fim':
                break

            if LeiaArq(nomearq) is None:
                print("Arquivo não encontrado. Digite novamente\n")
                continue

            nomearq_saida = input("Arquivo de saída: ")
            print()

        except:
            print("Erro no arquivo. Tente novamente.\n")
            continue

        else:

            ordem = verifica_entrada()

            if ordem is None:
                break

            elif len(ordem) == 1:
                print("\nOrdem da classificação: ", ordem[0], "\n\n")

            elif len(ordem) == 2:
                print("\nOrdem da classificação: ", ordem[0], ordem[1], "\n\n")

            elif len(ordem) == 3:
                print("\nOrdem da classificação: ", ordem[0], ordem[1], ordem[2], "\n\n")

            #Ler o arquivo de origem e colocar em TAB (já com split(‘,’) dos campos)
            lista_inicio = LeiaArq(nomearq)

            TAB1 = matriz_infos(lista_inicio)
            TAB2 = matriz_infos(lista_inicio)


            #Classifica1(TAB, ordem) – cronometrar e mostrar o tempo gasto
            t1 = time.process_time()
            Classifica1(TAB1, ordem)
            t2 = time.process_time()
            print("Tempo de classificação método 1 = ", t2 - t1, "\n")

            #Classifica2(TAB, ordem) – cronometrar e mostrar o tempo gasto
            t1 = time.process_time()
            Classifica2(TAB2, ordem)
            t2 = time.process_time()
            print("Tempo de classificação método 2 = ", t2 - t1, "\n")

            #Escreve o arquivo no mesmo formato que o de entrada
            escreve_arquivo(nomearq_saida, TAB2)
            print()



#Execução da main
main()
