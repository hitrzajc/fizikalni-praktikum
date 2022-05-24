from sys import stdin
def f(x):
    return 0.0206*x*x + 0.2539*x + 0.5821

inn = stdin.readlines()
x = [float(i) for i in inn]
#y = [f(i) for i in x]
for i in x:
    print(f(i))