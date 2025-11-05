import sys

def ler_tarefas()->list[list[float,float]]:

    """lê as tarefas do arquivo tasks.txt"""
    tarefas_lidas = []
    try:
        #'/home/hugosantos/VsCode/temp/algorithm-paradigms/greedy/tasks.txt'
        with open('tasks.txt', 'r') as arquivo:
            numero_tarefas = int(arquivo.readline().strip())
            for tarefa in range(numero_tarefas):
                #cada tarefa é uma lista 
                #no formato [tempo_inicio, tempo_fim]
                linha = arquivo.readline().strip()
                tarefa = linha.split()
                tarefa[0] = float(tarefa[0]) 
                tarefa[1] = float(tarefa[1])
                tarefas_lidas.append(tarefa)
    except:
        print("confira o caminho do arquivo")
        exit()
    # """lê as tarefas da entrada padrão """
    # tarefas_lidas = []
    # numero_tarefas = int(input())
    # for tarefa in range(numero_tarefas):

    #     #cada tarefa é uma lista 
    #     #no formato [tempo_inicio, tempo_fim]

    #     tarefa = input().split()
    #     tarefa[0] = float(tarefa[0]) 
    #     tarefa[1] = float(tarefa[1])
    #     tarefas_lidas.append(tarefa)
    
    return tarefas_lidas

def agenda_tarefas(tarefas : list)->list:
    """maximiza o número de tarefas que não se sobrepõem"""
    
    if not tarefas:
        return []
        

    _tarefas = sorted(tarefas[:], key= lambda x:x[1])
    print(f"tarefas ordenadas por f(t):\n{_tarefas}\n")

    tarefas_agendadas = []
    
    tarefas_agendadas.append(_tarefas[0])
    
    # tempo de fim da última tarefa agendada
    ultimo_fim = _tarefas[0][1]

    for tarefa in _tarefas[1:]:
        
       #verifica compatibilidade
        if tarefa[0] >= ultimo_fim:
            
            tarefas_agendadas.append(tarefa)
            ultimo_fim = tarefa[1]
                
    return tarefas_agendadas

def _profundidade(_tarefas): 
    
    tarefas_ordenadas = sorted(_tarefas, key=lambda x: x[0])
    
    n = len(tarefas_ordenadas)
    if n == 0:
        return 0
        
    profundidade_max = 0
    
    for i in range(n):
        
        ponto_de_verificacao = tarefas_ordenadas[i][0]
        
        profundidade_atual = 0
        
        for j in range(n):
            s_j = tarefas_ordenadas[j][0]
            f_j = tarefas_ordenadas[j][1]
            
            if s_j <= ponto_de_verificacao and f_j > ponto_de_verificacao:
                profundidade_atual += 1
                
        
        if profundidade_atual > profundidade_max:
            profundidade_max = profundidade_atual
            
    return profundidade_max

def agenda_tarefas_mult_recursos(tarefas : list)-> dict:
    

    _tarefas = sorted(tarefas, key=lambda x:x[0])
    n = len(_tarefas)
    

    agendamento = {} 
    

    for i in range(1, n + 1):
        
        s_i, f_i = _tarefas[i-1]
        

        recursos_conflitantes = set()
        

        for j in range(1, i):
            
            s_j, f_j = _tarefas[j-1]
            
            if s_i < f_j:

                recursos_conflitantes.add(agendamento[j])
        
        recurso_id = 1
        while True:
            if recurso_id not in recursos_conflitantes:

                agendamento[i] = recurso_id
                break 
                
            recurso_id += 1 
            
    return agendamento


def main():
    tarefas = ler_tarefas()
    print(f"tarefas lidas: \n{tarefas}\n")
    tarefas_agendadas = agenda_tarefas(tarefas)
    print(f"tarefas agendadas sem sobreposição:\n{tarefas_agendadas}\n")
    #print(profundidade(tarefas))
    tarefas_mult_recursos = agenda_tarefas_mult_recursos(tarefas)
    print(f"tarefas agendadas para vários recursos: \n{tarefas_mult_recursos}\n")

if __name__ == "__main__":
    main()