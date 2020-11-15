# def compara_linhas1(matriz1, matriz2, index1):
#
#     for i in range(len(matriz1)):
#
#         if matriz1[i][index1] != matriz2[i][index1]:
#             print("DIFERENTES::::", matriz1[i], matriz2[i], i)
#             return False
#
#     return True
#
# def compara_linhas2(matriz1, matriz2, index1, index2):
#
#     for i in range(len(matriz1)):
#
#         if matriz1[i][index1] != matriz2[i][index1] or matriz1[i][index2] != matriz2[i][index2]:
#             print("DIFERENTES::::", matriz1[i], matriz2[i], i)
#             return False
#
#     return True
#
# def compara_linhas3(matriz1, matriz2, index1, index2, index3):
#
#     for i in range(len(matriz1)):
#
#         if matriz1[i][index1] != matriz2[i][index1] or matriz1[i][index2] != matriz2[i][index2] or matriz1[i][index3] != matriz2[i][index3]:
#             print("DIFERENTES::::", matriz1[i], matriz2[i], i)
#             return False
#
#     return True

#ordem = ['0']
#ordem = ['1']
#ordem = ['2']

#ordem = ['0', '1']
#ordem = ['0', '2']
#ordem = ['1', '0']
#ordem = ['1', '2']
#ordem = ['2', '0']
#ordem = ['2', '1']

#ordem = ['0', '1', '2']   #OK
#ordem = ['0', '2', '1']   #OK
#ordem = ['1', '0', '2']   #OK
#ordem = ['1', '2', '0']   #OK
#ordem = ['2', '1', '0']   #OK
#ordem = ['2', '0', '1']   #OK

    '''
    if len(ordem) == 1:
        print("\n\n", compara_linhas1(matriz1, matriz2, int(ordem[0])), "\n\n")

    elif len(ordem) == 2:
        print("\n\n", compara_linhas2(matriz1, matriz2, int(ordem[0]), int(ordem[1])), "\n\n")

    else:
        print("\n\n", compara_linhas3(matriz1, matriz2, int(ordem[0]), int(ordem[1]), int(ordem[2])), "\n\n")

    '''
