

def ler_tarefas()->list[list[float,float]]:

    """lê as tarefas do arquivo tasks.txt"""
    tarefas_lidas = []
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
    #ordena as tarefas por tempo de finalização
    _tarefas = sorted(tarefas[:], key= lambda x:x[1])
    
    tarefas_agendadas = []
    print(f"tarefas ordenadas por f(t): \n: {_tarefas}")
    indice = 0
    while(_tarefas):
        tarefa_escolhida = _tarefas[indice]
        tarefas_agendadas.append(tarefa_escolhida)
        i = 0 #indice para popar da lista
        for tarefa in _tarefas:
            if tarefa[0] < tarefa_escolhida[1]:
                _tarefas.pop(i)
        indice+=1

    return tarefas_agendadas

def main():
    tarefas = ler_tarefas()
    print(tarefas)
    tarefas_agendadas = agenda_tarefas(tarefas)
    print(f"\n\n{tarefas_agendadas}")
if __name__ == "__main__":
    main()