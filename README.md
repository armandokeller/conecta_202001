# Conecta+ 2020/01 - Programação em Python (Básico)

## Recursos necessários
Interpretador online:
  - Para o primeiro exemplo: https://repl.it/languages/python_turtle
  - Para o segundo exemplo e demais códigos: https://repl.it/languages/python3
  
## Exemplo 1 - Utilizando o Turtle
O objetivo deste exemplo é demonstrar como as variáveis e as funções são interpretadas no Python

Neste exemplo vamos utilizar a biblioteca [Turtle](https://docs.python.org/3.3/library/turtle.html?highlight=turtle)
para desenhar formas geométricas.

Para importar uma biblioteca em python precisamos utilizar o comando import, normalmente estas importações
ocorrem no início do arquivo

```python
import turtle
```

Após isto precisamos criar um objeto Turtle, que será responsável por desenhar as formas geométricas.

```pyhton
t = turtle.Turtle()
```

Alguns comandos úteis do Turtle:

```python
# Rotacionar o cursor para a direita, passando o ângulo de rotação como parâmetro
t.rt(angulo)

# Rotacionar o cursor para a esquerda, passando o ângulo de rotação como parâmetro
t.lt(angulo)

# Andar para a frente, passando a distância a ser percorrida
t.fd(distancia)

# Levantar a caneta, isto permite que o cursor se mova sem desenhar
t.penup()

# Baixar a caneta, isto faz o cursor voltar a desenhar quando se move
t.pendown()

# Mover o cursor para uma posicao específica em x (pos_x) e em y (pos_y)
t.goto(pos_x, pos_y) 
```

### Desenhando um quadrado

Para desenhar um quadrado traçamos uma linha com uma determinada distância, rotacionamos o cursor em 90 graus, e repetimos
estes passos mais 3 vezes para completar o quadrado.

Vamos deixar a distância a ser percorrida armazenada em uma variável, para que seja mais fácil de alterar este valor

```python
distancia = 100
```

Agora podemos fazer o procedimento de desenho

```python
# Linha de baixo
t.fd(distancia)
t.lt(distancia)

# Linha da esquerda
t.fd(distancia)
t.lt(distancia)

# Linha de cima
t.fd(distancia)
t.lt(distancia)

# Linha da direita
t.fd(distancia)
t.lt(distancia)
```

A repetição destes passos pode ser resumida com laços de repetição

Temos dois tipos de laços de repetição o FOR e o WHILE

Utilizando o FOR
```python
for i in range(4):
  t.fd(distancia)
  t.lt(distancia)
```

Utilizando o WHILE
```python
# Utilizando for
i = 0
while i<4:
  t.fd(distancia)
  t.lt(distancia)
  i = i + 1
```

## Exemplo 2 - Carregando dados e plotando gráficos

Os dados de consumo de energia foram extraídos de https://dados.fee.tche.br
