import os
import math

def ler_pontos()->list:
    """lê os pontos (x, y) de um arquivo.txt"""
    lista_de_pontos = []
    diretorio_atual = os.path.dirname(os.path.realpath(__file__))
    caminho_entrada = os.path.join(diretorio_atual, "pontos.txt")
    with open(caminho_entrada) as arquivo:
        for linha in arquivo:
            ponto = linha.split(',')
            ponto = (float(ponto[0]), float(ponto[1]))
            lista_de_pontos.append(ponto)
    
def ordena_pontos(pontos)->tuple[list,list]:
    """retorna Px e Py"""
    pontos_x = sorted(pontos)
    pontos_y = sorted(pontos, key= lambda y:y[1])
    return (pontos_x, pontos_y)

def distancia(p1, p2):
    """retorna a distância Euclidiana entre dois pontos (x, y)"""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def forca_bruta(pontos):
    """
    encontra o par mais próximo em uma lista pequena (caso base).
    Retorna (distancia_minima, (ponto1, ponto2))
    """
    dist_min = float('inf')
    par_min = (None, None)
    
  #só é usado quando n<=3
    for i in range(len(pontos)):
        for j in range(i + 1, len(pontos)):
            d = distancia(pontos[i], pontos[j])
            if d < dist_min:
                dist_min = d
                par_min = (pontos[i], pontos[j])
                
    return (dist_min, par_min)
    
def encontra_par_mais_proximo(pontos_x, pontos_y:list):
   
    tamanho = len(pontos_x)
    if(tamanho<=3):
        return forca_bruta(pontos_x, pontos_y)
    
    meio_dos_pontos = tamanho // 2
    
    if (tamanho%2 != 0):
        mediana = pontos_x[meio_dos_pontos][0]
    else:
        mediana = (pontos_x[meio_dos_pontos][0] + pontos_x[meio_dos_pontos+1][0]) / 2
    
    pontos_ex = pontos_x[:meio_dos_pontos]
    pontos_dx = pontos_x[meio_dos_pontos:]
    pontos_ey = []
    pontos_dy = []
    
    for ponto in pontos_y:
        
        if ponto[0] <= mediana:
            pontos_ey.append(ponto)
        else:
            pontos_dy.append(ponto)
            
    (dist_E, par_E) = encontra_par_mais_proximo(pontos_ex, pontos_ey)
    (dist_D, par_D) = encontra_par_mais_proximo(pontos_dy, pontos_dy)

    dist_minima = min(dist_E, dist_D)
    if dist_E < dist_D:
        par_minimo = par_E
    else:
        par_minimo = par_D

    faixa = []
    for ponto in pontos_y:
        if abs(ponto[0] - mediana) < dist_minima:
            faixa.append(ponto)

    n_faixa = len(faixa)
    for i in range(n_faixa):
        #verificação dos <=7 pontos
        for j in range(i + 1, n_faixa):
            p1 = faixa[i]
            p2 = faixa[j]
            
            if (p2[1] - p1[1]) >= dist_minima:
                break
                
            d = distancia(p1, p2)
            if d < dist_minima:
                dist_minima = d
                par_minimo = (p1, p2)
                
    return (dist_minima, par_minimo)

def main():
    lista_pontos = ler_pontos()
    encontra_par_mais_proximo(lista_pontos)
    
    
if __name__ == "__main__":
    main()