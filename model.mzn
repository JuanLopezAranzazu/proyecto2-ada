% Integrantes del grupo:
% - Victor Manuel Álzate Morales - 202313022
% - Juan Esteban López Aránzazu - 202313026
% - Daniel Meléndez Ramirez - 202313024
% - Diego Alejandro Tolosa Sanchez - 202313023

% Variables
int: n; % Tamaño de las matrices
array[1..n, 1..n] of int: population; % Matriz de segmento de población
array[1..n, 1..n] of int: enterprise; % Matriz de entorno empresarial

int: programs; % Cantidad de programas que ya existen
array[1..programs, 1..2] of int: positions; % Coordenadas de los programas existentes

int: new_programs; % Cantidad de nuevos programas a ubicar

% Coordenadas de los nuevos programas
array[1..new_programs, 1..2] of var 1..n: new_positions;


% Función para calcular la suma de una celda y sus vecinas
function int: sum_neighbors(int: x, int: y, array[1..n, 1..n] of int: matrix) =
  sum(
    i in max(1, x-1)..min(n, x+1),
    j in max(1, y-1)..min(n, y+1)
  ) (
    matrix[i, j]
  );

% Función para verificar si dos puntos son adyacentes
function var bool: is_adjacent(var int: x1, var int: y1, var int: x2, var int: y2) =
  abs(x1 - x2) <= 1 /\ abs(y1 - y2) <= 1;


% Matriz precalculada para el segmento de población
array[1..n, 1..n] of int: population_neighbors = array2d(1..n, 1..n, [
  sum_neighbors(x, y, population)
  | x in 1..n, y in 1..n
]);

% Matriz precalculada para el entorno empresarial
array[1..n, 1..n] of int: enterprise_neighbors = array2d(1..n, 1..n, [
  sum_neighbors(x, y, enterprise)
  | x in 1..n, y in 1..n
]);


% Restricciones
constraint 
  % Los nuevos programas no pueden ser contiguos a los existentes
  forall(i in 1..new_programs, j in 1..programs) (
    not is_adjacent(new_positions[i, 1], new_positions[i, 2],
                    positions[j, 1], positions[j, 2])
  ) /\

  % Los nuevos programas no pueden ser contiguos entre sí
  forall(i in 1..new_programs, j in i+1..new_programs) (
    not is_adjacent(new_positions[i, 1], new_positions[i, 2],
                    new_positions[j, 1], new_positions[j, 2])
  ) /\

  % La suma del segmento de población debe ser al menos 25
  forall(i in 1..new_programs) (
    population_neighbors[new_positions[i, 1], new_positions[i, 2]] >= 25
  ) /\

  % La suma del entorno empresarial debe ser al menos 20
  forall(i in 1..new_programs) (
    enterprise_neighbors[new_positions[i, 1], new_positions[i, 2]] >= 20
  );

% Maximizar la suma combinada del segmento de población y entorno empresarial
var int: total_score = 
  sum(i in 1..new_programs)( 
    population_neighbors[new_positions[i, 1], new_positions[i, 2]] + 
    enterprise_neighbors[new_positions[i, 1], new_positions[i, 2]]
  );

% Ganancia total antes de las nuevas localizaciones
var int: existing_score = 
  sum(i in 1..programs)( 
    population_neighbors[positions[i, 1], positions[i, 2]] + 
    enterprise_neighbors[positions[i, 1], positions[i, 2]]
  );

% Ganancia total después de las nuevas localizaciones
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

