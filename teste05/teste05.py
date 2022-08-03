print('_'*20)
print('INVERSOR DE PALAVRAS')
print('_'*20)

palavra=input('Digite uma palavra: ')
palavra=palavra.upper()

if not palavra.isalpha():
    print('Você precisa digitar apenas letras.')
    palavra=input('Digite uma palavra: ')
else:
    inversao=palavra[::-1]
    print(f'Palavra digitada = {palavra}.')
    print(f'Palavra invertida = {inversao}')