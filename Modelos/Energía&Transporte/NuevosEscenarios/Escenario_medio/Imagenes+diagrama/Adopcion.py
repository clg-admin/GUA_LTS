# -*- coding: utf-8 -*-
import subprocess
from tqdm import tqdm
import os
import time
import pandas as pd

home = os.getcwd()
print(home)

# %%
# Este es funcional
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt


def generalized_logistic_curve(x, L, Q, k, M):
    return L / (1 + Q * math.exp(-k * (x - M)))

name = 'Heavy Hydrogen'
alias = 'TRYTKHYD'
R2050 = 0.99
L = 0.005
C = 0.003
M = 2045
Initial_Year_of_Uncertainty = 2024

r2050 = 1 / R2050
Q = L / C - 1
k = np.log((r2050 - 1) / Q) / (M - 2050)



# print(shift_years)
shift_years = [n for n in range(Initial_Year_of_Uncertainty + 1, 2050 + 1)]
shift_year_counter = 0
adoption_shift = []
#
for t in shift_years:
    x = int(shift_years[shift_year_counter])
    adoption_shift.append(generalized_logistic_curve(x, L, Q, k, M))
    shift_year_counter += 1

# test



# print(adoption_shift)

# Plot the adoption shift curve
plt.plot(shift_years, adoption_shift)
plt.xlabel("Year")
plt.ylabel("Adoption Shift")
# plt.title(f"Curva de adopción de estufas eficientes {L*100}% al 2050")
plt.title(f"Curva de adopción {name} {round(L*100)}% al 2050")
plt.plot([M], [C], 'o')
plt.annotate(f"{C * 100}% by {M}%", xy=(M, C), xytext=(M +1, C))
# save image of the curve
plt.savefig(f'{home}/{alias}_{int(L*100)}.png')

plt.show()

# make a dataframe with the values of the curve with the years and the values as a column
adoption_shift_df = pd.DataFrame(adoption_shift, columns=['Adoption_Shift'])
adoption_shift_df['Year'] = shift_years
print(adoption_shift_df)
# #
# # # save to csv
# adoption_shift_df.to_csv(f'/Users/edmiranda/Documents/Trabajo 2021/Investigación/Descarbonizacion/Parte 2/Modelo_2024/Base de datos/Adoption_curvs/{alias}{L*100}.csv', index=False)


