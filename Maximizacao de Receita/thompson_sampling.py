# Maximizando a Receita de um Neg�cio de Varejo On-Line

# Importacao das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import random

# Configuracao dos parametros
N = 10000
d = 9

# Criacao da simulacao
convertion_rates = [0.05, 0.13, 0.09, 0.16, 0.11, 0.04, 0.20, 0.08, 0.01]
X = np.array(np.zeros([N, d]))
for i in range(N):
    for j in range(d):
        if np.random.rand() <= convertion_rates[j]:
            X[i,j] = 1
            
# Implementacao da estrategia randomica e do Thompson Sampling
strategies_selected_rs = []
strategies_selected_ts = []
total_reward_rs = 0
total_reward_ts = 0
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d

for n in range(0, N):
    # Estrategia randomica
    strategy_rs = random.randrange(d)
    strategies_selected_rs.append(strategy_rs)
    reward_rs = X[n, strategy_rs]
    total_reward_rs += reward_rs
    
    # Thompson Sampling
    strategy_ts = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            strategy_ts = i
    reward_ts = X[n, strategy_ts]
    if reward_ts == 1:
        numbers_of_rewards_1[strategy_ts] += 1
    else:
       numbers_of_rewards_0[strategy_ts] += 1
    strategies_selected_ts.append(strategy_ts)
    total_reward_ts += reward_ts
    
# Calculo do retorno absoluto e retorno relativo
absolute_return = (total_reward_ts - total_reward_rs) * 19.99
relative_return = (total_reward_ts - total_reward_rs) / total_reward_rs * 100
print("Retorno Absoluto: {:.0f} R$".format(absolute_return))
print("Retorno Relativo: {:.0f} %".format(relative_return))

# Grafico com o histograma das selecaes
plt.hist(strategies_selected_ts)
plt.title('Histograma de seleções')
plt.xlabel('Strategy')
plt.ylabel('Number of times the strategy was selected')
plt.show()            
            
        
        
    































        