% datos de entrada
int: n; % tamaño de las matrices
array[1..n, 1..n] of int: population; % matriz de segmento de poblacion
array[1..n, 1..n] of int: enterprise; % matriz de entorno empresarial

int: programs; % cantidad de programas que ya existen
array[1..programs, 1..2] of int: positions; % coordenadas de los programas existentes

int: new_programs; % cantidad de nuevos programas a ubicar

% coordenadas de los nuevos programas
array[1..new_programs, 1..2] of var 1..n: new_positions;

% mostrar los datos de entrada
output ["Tamaño de las matrices = ", show(n), "\n"];
output ["Matriz de segmento de población = ", show(population), "\n"];
output ["Matriz de entorno empresarial = ", show(enterprise), "\n"];
output ["Cantidad de programas existentes = ", show(programs), "\n"];
output ["Coordenadas de los programas existentes = ", show(positions), "\n"];
output ["Cantidad de nuevos programas = ", show(new_programs), "\n"];

% mostrar los datos de salida
output ["Coordenadas de los nuevos programas = ", show(new_positions), "\n"];
