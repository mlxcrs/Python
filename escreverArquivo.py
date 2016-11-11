# -*- coding: latin-1 -*-
import random
# Cria um arquivo com 25 números randômicos
with file('temp.txt', 'w') as temp:
    for y in range(5):
        for x in range(5):
            # "print >> " grava a saída do comando no arquivo indicado
            print >> temp, '%.2f' % random.random(),
            print >> temp
# Exibe o conteúdo do arquivo
with file('temp.txt') as temp:
    for i in temp:
        print i,
# Fora dos blocos, o arquivo está fechado
# Isso gera uma exceção ValueError: I/O operation on closed file
print >> temp