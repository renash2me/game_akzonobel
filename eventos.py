#Importa random
import random

def sortear_eventos(turno, eventos, num_max_pacientes_por_evento):
    quantidade_eventos = turno * 2

    eventos_ponderados = []
    for evento in eventos:
        peso = evento["percentual_ocorrencias"]
        eventos_ponderados.extend([evento] * int(peso * 10))

    eventos_sorteados = random.sample(eventos_ponderados, quantidade_eventos)

      # Adiciona o número de pacientes afetados a cada evento sorteado
    for evento in eventos_sorteados:
        cor_evento = evento["cor"]

        # Limita o número de pacientes com base na cor do evento
        if cor_evento == "azul":
            evento["num_pacientes_afetados"] = random.choice([1, 2, 4, 8])
        elif cor_evento == "amarelo":
            evento["num_pacientes_afetados"] = random.choice([1, 2])
        elif cor_evento == "vermelho":
            evento["num_pacientes_afetados"] = 1

        # Imprimir os eventos sorteados em linhas separadas
    for evento in eventos_sorteados:
        for chave, valor in evento.items():
            if chave != 'percentual_ocorrencias':
                print(f'{chave}: {valor}')
        print()  # Adiciona uma linha em branco entre os eventos

    return eventos_sorteados

# Informações sobre eventos
eventos = [
    {"tipo": "gripe", "cor": "azul", "faturamento": int(100), "profissional": "clínico_geral", "estrutura": "enfermaria", "percentual_ocorrencias": float(18)},
    {"tipo": "resfriado", "cor": "azul", "faturamento": int(100), "profissional": "clínico_geral", "estrutura": "enfermaria", "percentual_ocorrencias": float(14)},
    {"tipo": "sopro", "cor": "azul", "faturamento": int(100), "profissional": "pediatra", "estrutura": "consultório", "percentual_ocorrencias": float(9)},
    {"tipo": "torsão_leve", "cor": "azul", "faturamento": int(100), "profissional": "ortopedista", "estrutura": "consultório+raioX", "percentual_ocorrencias": float(7)},
    {"tipo": "torsão_grave", "cor": "azul", "faturamento": int(100), "profissional": "ortopedista", "estrutura": "consultório+salaGesso", "percentual_ocorrencias": float(11)},
    {"tipo": "acidente_leve", "cor": "azul", "faturamento": int(100), "profissional": "ortopedista", "estrutura": "consultório+salaGesso", "percentual_ocorrencias": float(4.5)},
    {"tipo": "intoxicacao_alimentar", "cor": "amarelo", "faturamento": int(250), "profissional": "gastroenterologista", "estrutura": "endoscopia", "percentual_ocorrencias": float(9)},
    {"tipo": "pressa_alta", "cor": "amarelo", "faturamento": int(250), "profissional": "cardiologista", "estrutura": "eletrocardiograma", "percentual_ocorrencias": float(9)},
    {"tipo": "acidente_grave", "cor": "amarelo", "faturamento": int(250), "profissional": "traumatologista", "estrutura": "ressonância", "percentual_ocorrencias": float(4.5)},
    {"tipo": "apendicite", "cor": "vermelho", "faturamento": int(500), "profissional": "cirurgião_geral", "estrutura": "centro_cirúrgico", "percentual_ocorrencias": float(4.5)},
    {"tipo": "infarto", "cor": "vermelho", "faturamento": int(500), "profissional": "cirurgião_cardiologista", "estrutura": "centro_cirúrgico", "percentual_ocorrencias": float(4.5)},
    {"tipo": "fratura_exposta", "cor": "vermelho", "faturamento": int(500), "profissional": "cirurgião_ortopédico", "estrutura": "centro_cirúrgico", "percentual_ocorrencias": float(4.5)},
]
