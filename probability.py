flips = 10
heads = 5
def x(x, y, z):
 return y
def sm(b, i, t):
 summ = 0
 if t == 1:
  sex = x
 else:
  sex = sm
 while b < i + 1:
  summ = summ + sex(0, b, t - 1)
  b += 1
 return summ



def f(x):
 return sm(0, flips - heads + 1, heads - 1)*(x)**heads*(1-x)**(flips - heads)


r = 0
def itg(x, y, z, n, sum, p):
 global r
 if x > y:
  a = r
  r = 0
  return a/sum
 else:
  if x > p and x + z < p + 0.11:
   r += f(x)*z
  return itg(x + z, y, z, n + 1, f(x)*z + sum, p)


print(itg(0, 1, 0.005, 0, 0, 0.5)*100)
