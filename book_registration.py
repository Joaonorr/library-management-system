#!/usr/bin/env python
# coding: utf-8

# Durante a aula, você foi apresentado à criação de dicionários em diversas situações. Então, chegou o momento de praticar, a partir do que você aprendeu, e utilizar dicionários como estrutura básica para resolver o seguinte problema:
# 
# Imagine que você foi contratado para construir o sistema de gerenciamento de uma livraria e é o responsável por criar um módulo/célula, que fará a leitura dos dados de livros, que serão título, gênero, subgênero, editora, número de cópias em loja e valor em reais. Além disso, você também é o responsável pelo módulo de apresentação dos livros disponíveis em loja, de acordo com a seguinte organização: ao apresentar todos os livros disponíveis, eles devem ser separados, primeiro, por gênero e depois por subgênero, seguindo a estrutura a seguir:
# 
# --- Gênero A ---
# 
# ------ Subgênero A.1 ------
# 
# Livro 01
# 
# Livro 02
# 
# ------ Subgênero A.2 ------
# 
# Livro 03
# 
# --- Gênero B ---
# 
# ------ Subgênero B.1 ------
# 
# Livro 04
# 
# ------ Subgênero B.2 ------
# 
# Livro 05
# 
# Livro 06
# 
# Tanto gênero quanto subgênero devem seguir uma ordem alfabética de apresentação, em que, dentro de um subgênero, os livros devem ser listados pela quantidade disponível em loja. Vamos lá?

# livros = {
#     'titulo':'',
#     'genero':'',
#     'subgenero':'',
#     'editora':'',
#     'copas':'',
#     'preco':''
# }

# In[177]:


acervo = {}


# In[209]:


livros = {}

livros['titulo'] = input('Digite o titulo do livro: ').capitalize()
livros['genero'] = input('Digite o genero do livro: ')
livros['subgenero'] = input('Digite o subgenero do livro: ')
livros['editora'] = input('Digite a editora do livro: ')
livros['copias'] = input('Digite a quantidade de copias do livro: ')
livros['preco'] = input('Digite o preço do livro: ')


# In[210]:


inicial = livros['genero']


# In[211]:


if inicial not in acervo:
    acervo[inicial] = []


# In[212]:


acervo[inicial].append(livros)


# In[213]:


print(acervo)


# In[253]:


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
                
        
    
        


# In[257]:


valores = {0: 'Oi', oi: 'Tchau', 2: '!', 'repeticao':3}
valores['tabulacao'] = '\n' 
print(valores[2]) 


# In[259]:


mensagem = input('Digite uma string qualquer: ')
ocorrencias = {}
for letra in mensagem:
    ocorrencias[letra] += 1


# In[ ]:




