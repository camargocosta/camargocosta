usuario = str(input('Qual o seu usuario? ')).capitalize()
lista_usuario = {
    'Luciano': 'luciano123',
    'Eduardo': 'eduardo123',
    'Marcelo': 'marcelo2000',
    'Ana Maria': 'anamaria12'
}

if usuario in lista_usuario:
     senha =  input('Qual a sua senha:')
     if senha == lista_usuario[usuario]:
       print('Acesso liberado')

else:
    print('Acesso negado')


