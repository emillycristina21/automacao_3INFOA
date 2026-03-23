

#lista de nomes 
nomes = ['Giovana', 'Matheus','Goão', 'Julia','Vitória', 'Pietro']

for indice, nome in enumerate(nomes):
    print(f'Estou no {indice} que possui o nome {nome}')
    if nome == 'Goão':
        nomes[indice] = 'João'

print(nomes)