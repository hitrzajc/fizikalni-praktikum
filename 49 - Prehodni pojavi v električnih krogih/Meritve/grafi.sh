#!/usr/bin/gnuplot -persist
set term png large size 800,600
set output "praznjenje.png"

tao = 1

f(x) = 12*exp(-(x)/tao)
fit f(x) 'praznjenje.txt' u 1:2 via tao
set ylabel "U[V]"
set xlabel "t[s]"
plot 'praznjenje.txt' ps 2, f(x) lw 3


set output "polnjenje.png"
tao = 1
f(x) = 3.2*(1-exp(-(x)/tao))
fit f(x) 'polnjenje.txt' u 1:2 via tao
plot 'polnjenje.txt' ps 2, f(x) lw 3


set output 'dusenje.png'
b = 1
f(x) = 15*exp(-(x)*b)
fit f(x) 'dusenje.txt' u 1:2 via b
plot 'dusenje.txt' ps 2, f(x) lw 3