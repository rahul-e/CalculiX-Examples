set term postscript landscape monochrom noenhanced 
#set term x11 
set out "graph_0.ps"
set grid
set title "File:solve.frd"
set xlabel " nr "
set ylabel " STEP "
plot "graph_0.out" using 1:2 title 'val1' with linespoints pt 1, "graph_0.out" using 1:3 title 'val2' with linespoints pt 2, "graph_0.out" using 1:4 title 'val3' with linespoints pt 3

