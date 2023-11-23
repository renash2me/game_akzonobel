#Importar bibliotecas
import pandas as pd
import threading
import time
from eventos import sortear_eventos, eventos

# Parâmetros iniciais
turnos = 10
faturamento = 0
caixa = 3000 #VALOR DO CAIXA INICIAL
bonus_por_turno = 500
num_max_pacientes_por_evento = 8
tempo_inicial = 60*60 # UMA HORA
tempo_restante = tempo_inicial


# Informações sobre estruturas
locais = [
    {"local": "clínica", "cor": "azul", "capacidade_estruturas": 3},
    {"local": "centro_de_saúde", "amarelo": "azul", "capacidade_estruturas": 6},
    {"local": "hospital", "cor": "vermelho", "capacidade_estruturas": 9},
]

# Informações sobre estruturas
estruturas = [
    {"estrutura": "enfermaria", "cor": "azul", "capacidade": 2, "quantidade": 3, "custo": 250},
    {"estrutura": "enfermaria", "cor": "azul", "capacidade": 4, "quantidade": 2, "custo": 600},
    {"estrutura": "enfermaria", "cor": "azul", "capacidade": 6, "quantidade": 1, "custo": 800},
    {"estrutura": "consultório", "cor": "azul", "capacidade": 1, "quantidade": 2, "custo": 250},
    {"estrutura": "consultório+raioX", "cor": "azul", "capacidade": 1, "quantidade": 3, "custo": 300},
    {"estrutura": "consultório+salaGesso", "cor": "azul", "capacidade": 1, "quantidade": 2, "custo": 300},
    {"estrutura": "consultório+salaGesso", "cor": "azul", "capacidade": 2, "quantidade": 1, "custo": 750},
    {"estrutura": "consultório+salaGesso", "cor": "azul", "capacidade": 3, "quantidade": 1, "custo": 1200},
    {"estrutura": "endoscopia", "cor": "amarelo", "capacidade": 1, "quantidade": 3, "custo": 1000},
    {"estrutura": "eletrocardiograma", "cor": "amarelo", "capacidade": 1, "quantidade": 3, "custo": 1000},
    {"estrutura": "ressonância", "cor": "amarelo", "capacidade": 1, "quantidade": 3, "custo": 1000},
    {"estrutura": "centro_cirúrgico", "cor": "vermelho", "capacidade": 1, "quantidade": 6, "custo": 1500},
]

# Informações sobre profissionais
profissionais = [
    {"tipo": "clínico_geral", "cor": "azul", "estrutura_necessaria": "enfermaria", "quantidade": 6, "custo": 50},
    {"tipo": "pediatra", "cor": "azul", "estrutura_necessaria": "consultório", "quantidade": 2, "custo": 50},
    {"tipo": "ortopedista", "cor": "azul", "estrutura_necessaria": "raio-X e salaGesso", "quantidade": 7, "custo": 75}, #Ver o que fazer referente a estrutura necessária
    {"tipo": "gastroenterologista", "cor": "amarelo", "estrutura_necessaria": "endoscopia", "quantidade": 3, "custo": 100},
    {"tipo": "cardiologista", "cor": "amarelo", "estrutura_necessaria": "eletrocardiograma", "quantidade": 3, "custo": 100},
    {"tipo": "traumatologista", "cor": "amarelo", "estrutura_necessaria": "ressonância", "quantidade": 3, "custo": 100},
    {"tipo": "cirurgião_geral", "cor": "vermelho", "estrutura_necessaria": "centro_cirúrgico", "quantidade": 2, "custo": 200},
    {"tipo": "cirurgião_cardiologista", "cor": "vermelho", "estrutura_necessaria": "centro_cirúrgico", "quantidade": 2, "custo": 200},
    {"tipo": "cirurgião_ortopédico", "cor": "vermelho", "estrutura_necessaria": "centro_cirúrgico", "quantidade": 2, "custo": 200},
]



# Função para lidar com a contagem do tempo do jogo
def contarTempo():
    global tempo_restante
    while tempo_restante > 0:
        time.sleep(1)
        tempo_restante -= 1


# INICIA CONTAGEM REGRESSIVA
thread_tempo = threading.Thread(target=contarTempo)
thread_tempo.start()


#Função que mostra o status atual do jogador
def mostraStatusAtual(turno, faturamento, caixa, tempo_restante):
    minutos, segundos = divmod(tempo_restante, 60)

    print("--------_INÍCIO DE TURNO_--------")
    print(f"Turno: {turno}")
    print(f"Tempo restante: {minutos}:{segundos}")
    print(f"Faturamento: {faturamento}")
    print(f"Dinheiro em caixa: {caixa}")
    # print(f"Sua estrutura atual é: {locais}")


#SISTEMA DE TURNO
for turno in range(1, turnos + 1):
    #MOSTRA CENÁRIO ATUAL
    mostraStatusAtual(turno, faturamento, caixa, tempo_restante)

    #MOSTRA OPÇÕES DE INVESTIMENTOS DISPONÍVEIS
    investimentosEstruturas = pd.DataFrame(estruturas)
    investimentosProfissionais = pd.DataFrame(profissionais)
    acao_investimento = input("\nVocê pode investir em estruturas e em profissionais. Digite 1 para verificar os investimentos disponíveis de estrutura, ou digite 2 para verificar os investimentos disponíveis de profissionais. Caso não queira verificar os investimentos, só precione Enter. ")
    
    if not acao_investimento:
        print("\nOk, vamos continuar.")
        print()  # Adiciona uma linha em branco entre os eventos
        evento_escolhido = sortear_eventos(turno, eventos, num_max_pacientes_por_evento)
        # print(f"\nAconteceu um evento: {evento_escolhido}")
    else:
        try:
            acao_investimento = int(acao_investimento)
            if acao_investimento == 1:
                print("\nInvestimentos em Estruturas:")
                investimentosEstruturas.columns = ["Estrutura", "Cor", "Capacidade", "Quantidade disponível", "Custo"]
                print(investimentosEstruturas)
            elif acao_investimento == 2:
                print("\nInvestimentos em Profissionais:")
                investimentosProfissionais.columns = ["Profissional", "Cor", "Estrutura em qual atende", "Quantidade disponível", "Custo"]
                print(investimentosProfissionais)
            else:
                print("Opção inválida. Por favor, digite 1, 2 ou pressione Enter para continuar.")
        except ValueError:
            print("Entrada inválida. Por favor, digite 1 para verificar os investimentos disponíveis de estrutura, ou digite 2 para verificar os investimentos disponíveis de profissionais. Caso não queira verificar os investimentos, só precione Enter. ")

    #AGUARDA AÇÃO DO JOGADOR
    acao = input("Caso queira investir em uma estrutura, digite o número correspondente ao investimento desejado. Caso contrário, tecle enter para voltar.")


# Espera a thread do tempo terminar antes de encerrar o programa
thread_tempo.join()

# GAME OVER
if tempo_restante == 0:
    print("--------_GAME OVER_--------")
print("--------_PARABÉNS, VOCÊ CHEGOU AO FIM DO GAME_--------")
