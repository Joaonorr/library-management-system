

acervo = {}

livros = {}

livros['titulo'] = input('Digite o titulo do livro: ').capitalize()
livros['genero'] = input('Digite o genero do livro: ')
livros['subgenero'] = input('Digite o subgenero do livro: ')
livros['editora'] = input('Digite a editora do livro: ')
livros['copias'] = input('Digite a quantidade de copias do livro: ')
livros['preco'] = input('Digite o preço do livro: ')

inicial = livros['genero']

if inicial not in acervo:
    acervo[inicial] = []

acervo[inicial].append(livros)

print(acervo)

for inicial in sorted(acervo):
    print('--- {} ---\n'.format(inicial))

    for livros in sorted(acervo[inicial], key=lambda sub : sub['subgenero']):
        if aux == livros['subgenero']:
            continue
        aux = livros['subgenero'] 
        print(' ------ {} ------ '.format(livros['subgenero']))
        print('')
        
        for livros in sorted(acervo[inicial], key=lambda sub : sub['subgenero']):

            print('{}'.format(livros['titulo']))
            print('')
                

valores = {0: 'Oi', oi: 'Tchau', 2: '!', 'repeticao':3}
valores['tabulacao'] = '\n' 
print(valores[2]) 


mensagem = input('Digite uma string qualquer: ')
ocorrencias = {}
for letra in mensagem:
    ocorrencias[letra] += 1





