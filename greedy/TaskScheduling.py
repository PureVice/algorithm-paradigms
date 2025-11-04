

def ler_tarefas()->list[list[float,float]]:

    """lê as tarefas do arquivo tasks.txt"""
    tarefas_lidas = []
    with open('/home/hugosantos/VsCode/temp/algorithm-paradigms/greedy/tasks.txt', 'r') as arquivo:
        numero_tarefas = int(arquivo.readline().strip())
        for tarefa in range(numero_tarefas):
            #cada tarefa é uma lista 
            #no formato [tempo_inicio, tempo_fim]
            linha = arquivo.readline().strip()
            tarefa = linha.split()
            tarefa[0] = float(tarefa[0]) 
            tarefa[1] = float(tarefa[1])
            tarefas_lidas.append(tarefa)

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

def main():
    tarefas = ler_tarefas()
    print(f"tarefas lidas: \n{tarefas}\n")
    tarefas_agendadas = agenda_tarefas(tarefas)
    print(f"tarefas agendadas sem sobreposição:\n{tarefas_agendadas}")
    
if __name__ == "__main__":
    main()