import pandas as pd
import datetime
import numpy as np
import transform as tf

df = pd.read_csv(
    "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv",
    index_col=0
    )
df

#datframe limpo
df_raw = df.loc[df["air_time"] > 0]

#função tempo de voo em horas
print(tf.tempo_voo_horas(df_raw['air_time']))

#função turno partida
print(tf.turno_partida(df_raw['hour']))