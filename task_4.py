# Задачу 4 решать с помощью функции. Есть ли статистически значимые различия в росте дочерей и матерей?
# 4) Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160

import scipy.stats as stats
import numpy as np

N_0 = 'Нет статистически значимых различий'
N_1 = 'Статистически значимые различия имеются'

x = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169])
y = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])

test = stats.ttest_ind(x, y)
stat, p = test[0], test[1]

# print(test)

alpha = 0.05
if p > alpha:
    print(N_0)
else:
    print(N_1)

