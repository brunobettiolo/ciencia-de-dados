import matplotlib.pyplot as plt

#importa a biblioteca pandas
import pandas as pd

def exibirGraficos():
    # Cria o dataframe
    df = pd.DataFrame({
        "Meses": ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'],
        "Temperaturas": [29, 31, 30, 28, 27, 25, 21, 24, 27, 28, 29, 33]
    })

    # Redimensionado o gráfico 
    plt.figure(figsize=[10.0, 5.0])

    # Criação do gráfico
    plt.plot(df['Meses'], df['Temperaturas'], color="purple")

    # Definições dos títulos 
    plt.title("Temperatura média ao longo do tempo")
    plt.xlabel("Meses")
    plt.ylabel("Temperatura")

    # Exibindo o gráfico 
    plt.show()
    plt.savefig('chart2.png')

    # Exibe no console consoles dados estatísticos 
    print(f'Temperaturas: \n{df['Temperaturas'].describe()}')