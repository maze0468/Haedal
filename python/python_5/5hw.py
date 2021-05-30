import turtle as t

with open ('turtle.txt', 'r') as f:
    lines = f.readlines()
    values = list(map(int, lines))

t.shape('turtle')

for i in range(0,7,1):
   if (i%2 == 0):
       t.forward(values[0])
   elif (i%2 != 0):
       t.left(values[1])
