n = input('Digite algo: ')

print(type(n))

print('Tem apenas números? >',n.isnumeric())
print('Tem apenas letras? >', n.isalpha())
print('Tem letras E números? >', n.isalnum())

