import pickle
import datetime

# Arte ASCII criada a partir de símbolos
arte_ascii = '''
 __  ___  _______________   ___  ___________   ____
 / / / / |/ /  _/_  __/ _ | / _ \/ __/ __/ _ | / __/
/ /_/ /    // /  / / / __ |/ , _/ _// _// __ |_\ \  
\____/_/|_/___/ /_/ /_/ |_/_/|_/___/_/ /_/ |_/___/  
                                                   
O Gerenciador das suas Tarefas!
'''
print(arte_ascii)

# Função para salvar a lista em um arquivo
def salvar_lista(lista):
    #Filtrar tarefas concluidas
    lista_nao_concluida = [tarefa for tarefa in lista if len(tarefa) <= 3]
    with open('lista_tarefas.pkl', 'wb') as arquivo:
        pickle.dump(lista_nao_concluida, arquivo)

# Função para carregar a lista do arquivo
def carregar_lista():
    try:
        with open('lista_tarefas.pkl', 'rb') as arquivo:
            lista = pickle.load(arquivo)
    except FileNotFoundError:
        lista = []
    return lista

# Carregar a lista existente ou criar uma nova
lista = carregar_lista()

while True:
    print('\n• [1] Adicionar uma tarefa')
    print('• [2] Ver tarefas')
    print('• [3] Remover uma tarefa')
    print('• [4] Editar uma tarefa')
    print('• [5] Marcar uma tarefa como concluída')
    print('• [6] SAIR')

    perg = int(input('\nEscolha uma opção: '))

    # Opção 1: Adicionar uma tarefa
    if perg == 1:
        add = input('→ Digite a tarefa que deseja adicionar: ')
        horario = input('→ Digite o horário que deseja realizar a tarefa: ')
        descricao = input('→ Digite a descrição da tarefa: ')
        tarefa = [add, horario, descricao]
        lista.append(tarefa)
        print(f'-→ Tarefa "{add}" adicionada na lista')
        salvar_lista(lista)  # Salvar a lista após adicionar uma tarefa

    # Opção 2: Ver tarefas
    elif perg == 2:
        formato = int(input('[1] Formato de Lista\n[2] Formato de Linhas\nDigite o formato desejado: '))
        if formato == 1:
            tarefas_formatadas = [f'{tarefa[0]} - Horário: {tarefa[1]} - Descrição: {tarefa[2]} {"✓ [Concluído]" if len(tarefa) > 3 else ""}' for indice, tarefa in enumerate(lista)]
            print(f'Lista de Tarefas: {tarefas_formatadas}')
        elif formato == 2:
            now = datetime.datetime.now().time()
            for indice, tarefa in enumerate(lista):
                nome = tarefa[0]
                horario = tarefa[1]
                conclusao = '✓ [Concluído]' if len(tarefa) > 3 else ''
                print(f'| {indice} | {nome} - Horário: {horario} - Descrição: {tarefa[2]} {conclusao}')
                hora_tarefa = datetime.datetime.strptime(horario, '%H:%M').time()
                if hora_tarefa <= now:
                    print(f'---→ EI!! VOCÊ ESTÁ ATRASADO(a) PARA "{nome}" ----')
                else:
                    diferenca_minutos = (hora_tarefa.hour - now.hour) * 60 + (hora_tarefa.minute - now.minute)
                    if diferenca_minutos == 60:
                        print(f'---→ FIQUE ESPERTO! FALTA 1 HORA PARA A(o) "{nome}" ----')
                    elif diferenca_minutos == 10:
                        print(f'---→ SE LIGA! FALTA 10 MINUTOS PARA A(o) "{nome}" ----')
        else:
            print('→ Formato inválido')
    # Opção 3: Remover uma tarefa
    elif perg == 3:
        for indice, tarefa in enumerate(lista):
            nome = tarefa[0]
            horario = tarefa[1]
            descricao = tarefa[2]
            print(f'| {indice} | {nome} - Horário: {horario} - Descrição: {descricao}')
        excluir = int(input('→ Digite o número da tarefa que deseja remover: '))
        if excluir < 0 or excluir >= len(lista):
            print('→ Número de tarefa inválido')
        else:
            nome_excluir = lista[excluir][0]
            horario_excluir = lista[excluir][1]
            descricao_excluir = lista[excluir][2]
            lista.pop(excluir)
            print(f'Tarefa "{nome_excluir}" - Horário: {horario_excluir} - Descrição: {descricao_excluir} removida da lista')
            salvar_lista(lista)  # Salvar a lista após remover uma tarefa

    # Opção 4: Editar uma tarefa
    elif perg == 4:
        for indice, tarefa in enumerate(lista):
            nome = tarefa[0]
            horario = tarefa[1]
            descricao = tarefa[2]
            print(f'| {indice} | {nome} - Horário: {horario} - Descrição: {descricao}')
        editar = int(input('→ Digite o número da tarefa que deseja editar: '))
        if editar < 0 or editar >= len(lista):
            print('→ Número de tarefa inválido')
        else:
            novo_nome = input('→ Digite o novo nome da tarefa: ')
            novo_horario = input('→ Digite o novo horário da tarefa: ')
            nova_descricao = input('→ Digite a nova descrição da tarefa:')
            lista[editar][0] = novo_nome
            lista[editar][1] = novo_horario
            lista[editar][2] = nova_descricao
            print(f'-→ Tarefa [{editar}] editada para "{novo_nome}" - Horário: {novo_horario} - Descrição: {nova_descricao}')
            salvar_lista(lista)  # Salvar a lista após editar uma tarefa

    # Opção 5: Marcar uma tarefa como concluída
    elif perg == 5:
        for indice, tarefa in enumerate(lista):
            print(f'| {indice} | - {tarefa[0]}')
        pos = int(input('→ Em que posição está a tarefa que foi concluída? '))
        print(f'-→ Tarefa {pos} foi concluída')
        lista[pos] = lista[pos] + ['✓ [Concluído]']
        salvar_lista(lista)  # Salvar a lista após marcar uma tarefa como concluída

    # Opção 6: Sair do programa
    elif perg == 6:
        break

    else:
        print('→ Opção inválida')

