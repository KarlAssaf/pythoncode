cock = [2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 10.1, 11.1, 12.1, 13.1, 14.1, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2, 10.2, 11.2, 12.2, 13.2, 14.2, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3, 10.3, 11.3, 12.3, 13.3, 14.3, 2.4, 3.4, 4.4, 5.4, 6.4, 7.4, 8.4, 9.4, 10.4, 11.4, 12.4, 13.4, 14.4]
brd = list(map(lambda x: float(x), input("board cards: ").split("/")))
h = list(map(lambda x: float(x), input("your hand: ").split("/")))
nb = int(input("number of players: "))
gay = 0
trans = 0
import numpy as np
def mas(arr):
 coc = 0
 indes = 0
 for i, x in enumerate(arr):
  if round(max(x)) + 1 > coc:
   coc = round(max(x))
   indes = i
 return(indes)
for i in brd:
 cock = np.delete(cock, list(cock).index(i), 0)
for i in h:
 cock = np.delete(cock, list(cock).index(i), 0)
def game(a, *args):
 jefx = list(map(lambda x: x, brd))
 for i in a:
  jefx.append(i)
 pls = list(args[0])
 pls.append(h)
 win = [0, -1, mas(pls)]
 anb = 0
 for ind, pl in enumerate(pls):
  x = jefx + list(pl)
  lanb = 0
  streak = 0
  for e, i in enumerate(x):
   for f, j in enumerate(x):
    if e != f and round(i) == round(j) and win[1] < 1:
     if lanb < 4:
      lanb += 1
     if round(i) > win[0] and lanb + 1 > anb:
      win[0] = i
      win[1] = 0
      win[2] = ind
  if lanb + 1 > anb:
   anb = lanb
  win[0] = 0
  for e, i in enumerate(x):
   for f, j in enumerate(x):
    for g, k in enumerate(x):
     if e != f and f != g and e != g and round(i) == round(j) and round(j) == round(k) and round(i) > win[0] and win[1] < 2:
      win[0] = i
      win[1] = 1
      win[2] = ind
  x.sort()
  for j, i in enumerate(x):
   if round(i) == round(x[j - 1]) + 1 and win[1] < 3:
    streak += 1
    if streak == 4:
     win[0] = i
     win[1] = 2
     win[2] = ind
   else:
    streak = 0
 global gay
 global trans
 trans += 1
 if win[2] == len(pls) - 1:
  gay += 1
def loop(arr, n, v):
 for i, a in enumerate(arr):
  y = np.delete(arr, i, 0)
  for j, b in enumerate(y):
   w = np.delete(y, j, 0)
   s = list(map(lambda x: x, v))
   args = []
   args.append(a)
   args.append(b)
   s.append(args)
   if n != 1:
    loop(w, n - 1, s)
   else:
    l = s.pop(0)
    game(l, s)
loop(cock, nb, [])
print(gay)
print(trans)
print(gay/trans)
