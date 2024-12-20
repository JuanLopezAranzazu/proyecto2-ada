% datos de entrada
int: n; % tamaño de las matrices
array[1..n, 1..n] of int: population; % matriz de segmento de poblacion
array[1..n, 1..n] of int: enterprise; % matriz de entorno empresarial

int: programs; % cantidad de programas que ya existen
array[1..programs, 1..2] of int: positions; % coordenadas de los programas existentes

int: new_programs; % cantidad de nuevos programas a ubicar

% coordenadas de los nuevos programas
array[1..new_programs, 1..2] of var 1..n: new_positions;

% mostrar los datos de salida
output [show(new_positions)];
