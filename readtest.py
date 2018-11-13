import numpy as np
np.set_printoptions(threshold=np.inf)
def readfile():
  with open('link2.net') as f:
    line = f.readlines();
  return line

list1=readfile()
flag = 1
node_sizes = 0
adj = np.zeros((107,107))
adx = np.zeros((107,107))
for i in list1:
  i.rstrip('\n')
  if (flag is 1):
    temp = i[10:]
    node_sizes = int(temp)
    flag+=1
    continue
  if (flag is 2):
    flag+=1
    continue
  for j in range(len(i)):
    if (i[j] is ' '):
      break
  flag+=1
  temp = i[:j]
  temp1 = i[j+1:]
  x = int(temp)
  y = int(temp1)
  adj[x,y] = 1
  adj[y,x] = 1
  adx[x,0] += 1
  adx[x,int(adx[x,0])] = y  
  adx[y,0] += 1
  adx[y,int(adx[y,0])] = x
pre=node_sizes
temp_sizes = node_sizes

while (True):
  for i in range(1,node_sizes+1):
    if (adx[i,0]<=3 and adx[i,0]!=0):
      temp_sizes = temp_sizes - 1
      for j in range(1,int(adx[i,0])+1):
        for k in range(1,int(adx[int(adx[i,j]),0])+1):
          if (int(adx[int(adx[i,j]),k]) is int(i)):
            temp3 = k
            while (temp3 != int(adx[int(adx[i,j]),0])):
              adx[int(adx[i,j]),temp3] = adx[int(adx[i,j]),temp3+1]
              temp3 = temp3 +1
        adx[int(adx[i,j]),0]=adx[int(adx[i,j]),0]-1      
      adx[i,0] = 0 
  if (pre is temp_sizes):
    break
  pre=temp_sizes 

for i in range(1,101):
  temp1 = int(adx[i,0])
  while (temp1>0):
    print(str(i)+' '+str(int(adx[i,temp1])))
    temp1 = temp1 - 1

