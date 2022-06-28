from tkinter import N


veiculos = ['ix35' , 'SantaFé' , 'EcoSport' , 'Porsche' , 'HondaCivic']
n1 = print('Digite para:[0] ix35 [1] SantaFé [2]EcoSport [3]Porsche [4]HondaCivic')
n2 = input('Escolha um CARRO:')
n3 = input('ix35 custa 60000') , ('SantaFé custa 80000') , ('Poscher custa 500000') , ('HondaCivic 45000')
print('Deseja Compra? ')
status = ['Disponivel' , 'indisponivel'] 
valores = [60000, 80000, 50000, 500000, 45000]
print('o ' , veiculos[1] ,'esta disponivel' , veiculos[3], 'esta Indisponivel',veiculos[2], ' esta disponivel', veiculos[0], 'esta disponivel' )
print(veiculos[0],'custa R$',valores[0] , 'Mil', veiculos[1],'custa R$',valores[1],'mil',veiculos[2],'custa R$', valores[4])