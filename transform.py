import pandas as pd

def tempo_voo_horas(coluna_tempo_voo):

  df = coluna_tempo_voo.map(lambda x: x/60)

  return df

'''
    
    Regra de classificação:
    06:00 - 12:00 : MANHÃ
    12:00 - 18:00 : TARDE
    18:00 - 00:00 : NOITE
    00:00 - 06:00 : MADRUGADA

    return coluna_turno
'''

def turno_partida(coluna_data_hora):

  return pd.cut(coluna_data_hora,
                  bins=[-1, 5, 11, 17, 23],
                  labels=['MADRUGADA', 'MANHÃ', 'TARDE', 'NOITE'])