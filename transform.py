import pandas as pd

def tempo_voo_horas(coluna_tempo_voo:pd.Series)-> str:
    '''Esta função converte os valores do tempo de voo de minutos para horas.

    Entrada:
    coluna_tempo_voo: Parâmetro contendo tempos de vôo em minutos.

    Saída:
    Dataframe com os tempos convertidos em horas.
'''

    df = coluna_tempo_voo.map(lambda x: x/60)
    
    return df


def turno_partida(coluna_data_hora:pd.Series)-> str:
   '''Esta função classifica horários do dia em turnos predefinidos conforme as regras abaixo:

    06:00 - 12:00 : MANHÃ
    12:00 - 18:00 : TARDE
    18:00 - 00:00 : NOITE
    00:00 - 06:00 : MADRUGADA
    
    Entrada:
    coluna_data_hora: Parâmetro contendo tempos de vôo em minutos.

    Saída:
    Dataframe com os turnos classificados
'''

   df = pd.cut(coluna_data_hora,
                  bins=[-1, 5, 11, 17, 23],
                  labels=['MADRUGADA', 'MANHÃ', 'TARDE', 'NOITE'])
   return df
   
