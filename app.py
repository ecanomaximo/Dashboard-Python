import sqlite3
import random
import matplotlib.pyplot as plt
import os

def gerar_personagem():
    personagens = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Bowser"]
    return random.choice(personagens)

conn = sqlite3.connect('personagens.db')
cursor = conn.cursor()

# Cria a tabela de personagens
cursor.execute('''CREATE TABLE IF NOT EXISTS tabela_personagens
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 numero_aleatorio INT,
                 personagem TEXT)''')

# Gera e insere 10 valores aleatórios na tabela de personagens
for _ in range(10):
    numero_aleatorio = random.randint(1, 100)
    personagem = gerar_personagem()
    cursor.execute("INSERT INTO tabela_personagens (numero_aleatorio, personagem) VALUES (?, ?)",
                   (numero_aleatorio, personagem))

# Cria a tabela de meses
cursor.execute('''CREATE TABLE IF NOT EXISTS tabela_meses
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 numero_aleatorio INT,
                 personagem TEXT,
                 mes TEXT)''')

for _ in range(10):
    mes = random.choice(['Janeiro', 'Fevereiro', 'Março'])
    numero_aleatorio = random.randint(1, 100)
    personagem = gerar_personagem()
    cursor.execute("INSERT INTO tabela_meses (numero_aleatorio, personagem, mes) VALUES (?, ?, ?)",
                   (numero_aleatorio, personagem, mes))


# Seleciona os dados da tabela de personagens
cursor.execute("SELECT numero_aleatorio, personagem FROM tabela_personagens")
data = cursor.fetchall()

# Indica o personagem com o pior número
pior_personagem = min(data, key=lambda x: x[0])[1]

numeros_aleatorios = [row[0] for row in data]
personagens = [row[1] for row in data]

# Cria o gráfico para a tabela de personagens
plt.figure(figsize=(10, 6))
bars = plt.barh(personagens, numeros_aleatorios, color='skyblue')
for bar, personagem in zip(bars, personagens):
    if personagem == pior_personagem:
        bar.set_color('red')

plt.xlabel('Número Aleatório')
plt.ylabel('Personagem')
plt.title('Números Aleatórios Associados a Personagens')
plt.gca().invert_yaxis()

# Seleciona os dados da tabela de meses
cursor.execute("SELECT numero_aleatorio, mes FROM tabela_meses")
data_meses = cursor.fetchall()

numeros_aleatorios_meses = [row[0] for row in data_meses]
meses = [row[1] for row in data_meses]

# Cria o gráfico para a tabela de meses
plt.figure(figsize=(10, 6))
bars_meses = plt.bar(meses, numeros_aleatorios_meses, color='lightgreen')
plt.xlabel('Mês')
plt.ylabel('Número Aleatório')
plt.title('Números Aleatórios por Mês')

plt.show()

# Exclui o banco de dados antigo
os.remove('personagens.db')