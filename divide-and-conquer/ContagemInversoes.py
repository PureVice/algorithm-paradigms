import os 

def ler_lista_de_arquivo():
    
    diretorio_atual = os.path.dirname(os.path.realpath(__file__))
    caminho_teste = os.path.join(diretorio_atual, "lista.txt")
    with open(caminho_teste, "r") as arquivo:
        lista = arquivo.read()
        lista = lista.split()
        for i in range(len(lista)):
            lista[i] = int(lista[i])
    return lista
            
def merge_and_count(L1, L2) -> tuple[int, list]:
    
    merged_list : list = []
    inversoes = ponteiro_L1 = ponteiro_L2 = 0
    tamanho_L1 = len(L1)
    tamanho_L2 = len(L2)
    
    while((tamanho_L1 - ponteiro_L1)>0 and (tamanho_L2 - ponteiro_L2)>0):
        elemento_L1 = L1[ponteiro_L1]
        elemento_L2 = L2[ponteiro_L2]
        if(elemento_L2 < elemento_L1):
            merged_list.append(elemento_L2)
            inversoes+= tamanho_L1 - ponteiro_L1
            ponteiro_L2+=1
        else:
            merged_list.append(elemento_L1)
            ponteiro_L1+=1

    if((tamanho_L1 - ponteiro_L1)<=0):
        merged_list = merged_list + L2[ponteiro_L2:]
    else:
        merged_list = merged_list + L1[ponteiro_L1:]

    return (inversoes, merged_list)

def sort_and_count(L:list):
    tamanho_lista = len(L)
    if  tamanho_lista <= 1:
        return (0, L)
    
    metade = tamanho_lista//2
    L1 = L[0:metade]
    L2 = L[metade:]

    inversoes1 : tuple[int, list] = sort_and_count(L1)
    inversoes2 : tuple[int, list] = sort_and_count(L2)
    inversoes : tuple[int, list] = merge_and_count(inversoes1[1], inversoes2[1]) 
    
    return (inversoes1[0] + inversoes2[0] + inversoes[0], inversoes[1])

def main():
    
    lista = ler_lista_de_arquivo()
    inversoes_lista = sort_and_count(lista)  
    print(inversoes_lista) 

if __name__ == "__main__":
    main()
