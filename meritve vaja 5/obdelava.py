from math import pi,e,sqrt
n_interval = 10
n = 50
l = []
for i in range(n):
    l.append(float(input()))

mi = min(l)
mx = max(l)
t = sum(l)/n #povprecna
o = max(mx-t,t-mi) #napaka


dx = (mx-mi)/n_interval
actual = [0]*n_interval
theor = actual.copy() #theory

for i in l:
    for j in range(1,n_interval+1):
        if(i<mi+dx*j):
            actual[j-1]+=1
            break

def gaus(tt):
    return pow(e,-(t-tt)**2/(2*o**2))/(sqrt(pi*2)*o)


d = n//n_interval #dolzina intervala
for i in range(n_interval):
    tt = sum(l[i*d:i*d+d])/d
    #print(tt)
    #theor[i] = round(gaus(tt)*dx*50)
    theor[i] = gaus(tt)*dx*n

print("actual")
for i in actual:
    print(i)
print("theoretical")
for i in theor:
    print(i)
