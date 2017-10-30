q = []
num=int(input("Enter number processes.."))
for x in range(num):
    a,b=map(int,input("Enter BT and AT=").split())
    q.append((a,b))

sorting = sorted(q, key=lambda tup:tup[1])
print(sorting)

l=len(sorting)
at =[]
for x in range(l):
    c=sorting[x][1]
    at.append(c)
print(at)

bt =[]
for x in range(l):
    c=sorting[x][0]
    bt.append(c)
print(bt)

l=len(bt)
cal=[0]
sumn=0

for x in range(l):
    sumn=sumn+bt[x]
    i=sumn
    cal.append(i)
print(cal)

del bt[:]

for i in range(l):
    b=cal[i+1]-at[i]
    bt.append(b)

total = sum(bt)
avgtat=total/l;
print("Average turn around time=",avgtat)

del bt[:]
for i in range(l):
    d=cal[i]-at[i]
    bt.append(d)

total = sum(bt)
avgwt =total/l;
print("Average waiting time=",avgwt)
