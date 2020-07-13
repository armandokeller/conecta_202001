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
t.lt(90)

# Linha da esquerda
t.fd(distancia)
t.lt(90)

# Linha de cima
t.fd(distancia)
t.lt(90)

# Linha da direita
t.fd(distancia)
t.lt(90)
```

A repetição destes passos pode ser resumida com laços de repetição

Temos dois tipos de laços de repetição o FOR e o WHILE

Utilizando o FOR
```python
for i in range(4):
  t.fd(distancia)
  t.lt(90)
```

Utilizando o WHILE
```python
# Utilizando for
i = 0
while i<4:
  t.fd(distancia)
  t.lt(90)
  i = i + 1
```

Podemos utilizar as funçoes para "empacotar" estes comandos, evitando a necessidade de repetir o código todas as vezes que quisermos desenhar um quadrado.

```python
def quadrado():
  for i in range(4):
    t.fd(distancia)
    t.lt(90)
 ```
 
 Para chamar uma função, basta chamar o nome dela
```python
quadrado()
```
É possivel passar argumentos para as funções, tornando o códiugo ainda mais flexivel.
Um exemplo de parâmetro que pode ser passado é a distância (que chamaremos de tamanho), permitindo que possamos criar quadrados de tamanhos diferentes.


```python
def quadrado(tamanho):
  for i in range(4):
    t.fd(tamanho)
    t.lt(90)
 
quadrado(10)
quadrado(20)
quadrado(50)
 ```

Para desenhar quadrados em posições específicas, devemos passar as coordenadas para a função, e cuidar para levantar a caneta antes de mover o cursor.


```python
def quadrado(tamanho, x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  for i in range(4):
    t.fd(tamanho)
    t.lt(90)

quadrado(20, 0, 0)
quadrado(20, 30, 0)
quadrado(20, 30, 30)
quadrado(20, 0, 30)
quadrado(70, -10, -10)
```


## Exemplo 2 - Carregando dados e plotando gráficos

Os dados de consumo de energia utilizados neste exemplo foram extraídos de https://dados.fee.tche.br

A linguagem python é bastante utilizada para ánálise de dados, então vamos buscar dados sobre consumo de energia nas cidades do estado
do Rio Grande do Sul e vamos comparar o consumo industrial e comercial com o consumo residêncial por município.

A biblioteca [pandas](https://pandas.pydata.org) é bastante utilizada para trabalhar com dados tabulares, assim como o Excel. Vamos utilizar esta biblioteca para poder manipular os dados com mais facilidade. Além desta biblioteca, utilizaremos a matplotlib, que será responsável por gerar gráficos dos nossos dados.

```python
import pandas as pd
import matplotlib.pyplot as plt
```

Os dados a serem importados estão no formato CSV (Comma Separated Values) e estão disponíveis neste repositório na pasta "energia_rs". É possível realizar o download dos arquivos, ou importar diretamente da internet.

```python
# Salvando o endereço do arquivo na variável URL
url ="https://github.com/armandokeller/conecta_202001/raw/master/energia_rs/energia_residencial.csv"

# Importando para a variável df_residencial
df_residencial = pd.read_csv(url,sep=";",encoding="ISO-8859-1",skiprows=6,index_col="Município")

# Gerando a lista com todos os anos disponíveis (de 1991 até 2018)
anos = list(df_residencial.columns)

# Realizando a transposição dos dados para que os municípios sejam as colunas e os anos as linhas
df_residencial = df_residencial.transpose()

# Criando a lista de cidades
cidades = list(df_residencial.columns)
```

O mesmo procedimento é realizado para o consumo industrial e comercial, agora sem a necessidade de criar a lista de anos disponíveis e de cidades, pois estas já foram criadas.

```python
# Dados industriais
url ="https://github.com/armandokeller/conecta_202001/raw/master/energia_rs/energia_industrial.csv"
df_industrial = pd.read_csv(url,sep=";",encoding="ISO-8859-1",skiprows=6,index_col="Município")
df_industrial = df_industrial.transpose()

# Dados comerciais
url ="https://github.com/armandokeller/conecta_202001/raw/master/energia_rs/energia_comercial.csv"
df_comercial = pd.read_csv(url,sep=";",encoding="ISO-8859-1",skiprows=6,index_col="Município")
df_comercial = df_comercial.transpose()
```
