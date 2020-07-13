import turtle

t = turtle.Turtle()

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