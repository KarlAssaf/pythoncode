flips = int(input("specify number of flips: "))
nofh = int(input("specify number of heads: "))
array = []
def mkarr():
 global array
 j = 0
 while j < flips:
  array.append(0)
  j += 1
 i = 1
 while i < flips + 1:
  if i < nofh + 1:
   array[i - 1] = i
  else:
   array[i - 1] = 0
  i += 1
mkarr()
all = 0
def t(x):
 if x != 0:
  return 1
 else:
  return 0
def pushleft(n, counter):
  nb = array.index(n)
  nx = array.index(n) + 1
  counter = counter
  print(list(map(t, array)))
  if nx < len(array):
   if array[nx] == 0:
    array[nb] = 0
    array[nx] = n
    counter += 1
    pushleft(n, counter)
  else:
    print(counter)
    global all
    all = all + counter
    if counter == 1:
     print("-----------------------------------------------------------------------------------------------")
    fix()
def check(numb):
 if array.index(numb) + 1 < len(array):
  if array[array.index(numb) + 1] == 0:
   return numb
  else:
   return check(numb - 1)
 else:
  return check(numb - 1)
def fix():
 p = check(max(array))
 if p == 0:
  print(all)
  return
 ip = array.index(p)
 array[ip] = 0
 array[ip + 1] = p
 ip += 2
 while ip < len(array):
  if array[ip] != 0:
   i = 1
   st = 0
   while st == 0:
    if array[ip - i] == 0:
     i += 1
    else:
     if array[ip - i + 1] != array[ip]:
      array[ip - i + 1] = array[ip]
      array[ip] = 0
     st += 1
   ip += 1
  else:
   ip += 1
 pushleft(max(array), 1)
pushleft(max(array), 1)
