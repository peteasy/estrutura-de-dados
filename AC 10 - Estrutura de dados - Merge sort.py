# Estrutura de dados
# Atividade Contínua 10
# Alunos:
    # André Niimi           RA 1600736
    # Caique Tuan           RA 1600707
    # Gustavo Andreotti     RA 1600044

#Linguagem de programação utilizada: Python

# inicio da função recursiva
def mergeSort(lista):
    
    # Dividindo a lista em duas partes
    if len(lista)>1:
        meio = len(lista)//2
        L = lista[:meio]
        R = lista[meio:]

        # Executando recursivamente a função da parte esquerda
        mergeSort(L)

        # Executando recursivamente a função da parte direita
        mergeSort(R)

        # Atribuindo o valor 0(zero) para as variáveis i, j e k
        i=0
        j=0
        k=0
        
        # Este while só será encerrado quando a variável i
        # for maior que a quantidade de números na parte esquerda
        # e a variável j for maior que a quantidade de números na
        # parte direita
        while i < len(L) and j < len(R):
            
            # Comparando os valores e decidindo qual valor será trocado
            if L[i] < R[j]:
                lista[k]=L[i]
                i=i+1
            else:
                lista[k]=R[j]
                j=j+1
            k=k+1
            
        # Atribuindo o menor valor na variável lista[posição atual]
        while i < len(L):
            lista[k]=L[i]
            i=i+1
            k=k+1
        # Atribuindo o menor valor na variável lista[posição atual]
        while j < len(R):
            lista[k]=R[j]
            j=j+1
            k=k+1
    
# Exibindo a lista sem ordenação
lista = [54,26,93,17,77,31,44,55,20]
print ("Lista sem MergeSort: ", lista)

# Exibindo a lista com ordenação
mergeSort(lista)
print ("Lista com MergeSort: ", lista)
