import numpy as np
import matplotlib.pyplot as plt

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)  # Grafico com colunas
# plt.plot(x, y) #grafico com linhas
# plt.pie(x, y)  # Grafico como uma pizza

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.title("Sports Wacth Data", fontdict=font1)
plt.xlabel("Eixo X", fontdict=font2)
plt.ylabel("Eixo Y", fontdict=font2)
plt.legend()
plt.show()
