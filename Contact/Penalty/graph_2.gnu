set term postscript landscape monochrom  
#set term x11 
set out "graph_2.ps"
set title "Values at Nodes (all.fbd)"
set grid
set ylabel " CPRESS   "
set xlabel " Time "
plot "graph_2.out" using 3:5 title 'Node=10' with linespoints
 