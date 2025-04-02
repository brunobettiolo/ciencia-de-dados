# Faz a importação da biblioteca matplotlib e adiciona um alias (apelido)
# Usar linha de comando : python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def ExibirGrafico():
    grupo = ['A','B','C']
valores = [23,38,12]
# Definição dos grupos e valores

# Configura em Gráfico de barra, onde recebe os grupo, valores
# # E opicional ao cores
plt.bar( grupo , valores, color=[ 'red', 'blue', 'gray'])

# grafico

plt.title('grafico de barras simples')

plt.xlabel('grupos')

#titulo eixo x