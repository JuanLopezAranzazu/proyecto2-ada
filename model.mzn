% datos de entrada
int: n; % tamaño de las matrices
array[1..n, 1..n] of int: population; % matriz de segmento de poblacion
array[1..n, 1..n] of int: enterprise; % matriz de entorno empresarial

int: programs; % cantidad de programas que ya existen
array[1..programs, 1..2] of int: positions; % coordenadas de los programas existentes

int: new_programs; % cantidad de nuevos programas a ubicar

% coordenadas de los nuevos programas
array[1..new_programs, 1..2] of var 1..n: new_positions;

% función para calcular la suma de una celda y las celdas adyacentes
function var int: sum_neighbors(array[1..n, 1..n] of int: matrix, var int: x, var int: y) =
  sum(
    i in max(1, x-1)..min(n, x+1),
    j in max(1, y-1)..min(n, y+1)
  ) (
    matrix[i, j]
  );

% restricciones del problema
constraint 
  % los nuevos programas no pueden ser contiguos a los existentes
  forall(i in 1..new_programs, j in 1..programs) (
    abs(new_positions[i, 1] - positions[j, 1]) > 1 \/ 
    abs(new_positions[i, 2] - positions[j, 2]) > 1
  ) /\

  % los nuevos programas no pueden ser contiguos entre sí
  forall(i in 1..new_programs, j in i+1..new_programs) (
    abs(new_positions[i, 1] - new_positions[j, 1]) > 1 \/ 
    abs(new_positions[i, 2] - new_positions[j, 2]) > 1
  ) /\

  % la suma del segmento de población debe ser al menos 25
  forall(i in 1..new_programs) (
    sum_neighbors(population, new_positions[i, 1], new_positions[i, 2]) >= 25
  ) /\

  % la suma del entorno empresarial debe ser al menos 20
  forall(i in 1..new_programs) (
    sum_neighbors(enterprise, new_positions[i, 1], new_positions[i, 2]) >= 20
  );

% maximizar la suma combinada del segmento de poblacion y entorno empresarial
var int: total_score = 
  sum(i in 1..new_programs)( 
    population[new_positions[i, 1], new_positions[i, 2]] + 
    enterprise[new_positions[i, 1], new_positions[i, 2]] 
  );

% ganancia total antes de las nuevas localizaciones
var int: existing_score = 
  sum(i in 1..programs)( 
    population[positions[i, 1], positions[i, 2]] + 
    enterprise[positions[i, 1], positions[i, 2]] 
  );

% ganancia total después de las nuevas localizaciones
var int: final_score = existing_score + total_score;

solve maximize total_score;

% Salida del modelo
output [
  "total_score = \(total_score)\n",
  "existing_score = \(existing_score)\n",
  "final_score = \(final_score)\n",
  "new_positions = \(new_positions)\n",
  "positions = \(positions)\n"
];