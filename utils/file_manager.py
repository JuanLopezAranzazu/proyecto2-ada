# leer los datos y guardar los resultados en archivos de texto

def load_data_from_file(file_path):
  """
  Carga los datos de un archivo de texto y devuelve las matrices y valores.

  Parámetros:
    file_path (str): Ruta al archivo de texto.
  
  Retorna:
    population (list[list[int]]): Matriz de segmentos de población.
    enterprise (list[list[int]]): Matriz de entornos empresarial.
    positions (list[list[int]]): Vector de posiciones de los programas existentes.
    new_programs (int): Cantidad de nuevos programas a ubicar.
    programs (int): Cantidad de programas existentes.
    n (int): Tamaño
  """
  try:
    with open(file_path, 'r') as file:
      lines = file.readlines()
      
      population = []  # matriz de segmentos de población
      enterprise = [] # matriz de entornos empresarial
      positions = [] # vector de posiciones de los programas existentes

      programs = int(lines[0].strip())

      # Cargar los datos de los programas
      for i in range(programs):
        positions.append(list(map(int, lines[i+1].strip().split())))

      n = int(lines[programs+1].strip())
      
      # Cargar los datos de la población y el entorno empresarial
      for i in range(n):
        population.append(list(map(int, lines[programs+2+i].strip().split())))
        enterprise.append(list(map(int, lines[programs+2+n+i].strip().split())))

      new_programs = int(lines[programs+2+2*n].strip())

      return population, enterprise, positions, new_programs, programs, n

  except Exception as e:
    raise Exception(f"Error al cargar el archivo: {e}")


def save_results_to_file(file_path, new_positions, positions, existing_score, total_score, final_score):
  """
  Guarda los resultados proporcionados en un archivo de texto.

  Parámetros:
    file_path (str): Ruta al archivo de texto.
    new_positions (list[list[int]]): Nuevas posiciones de los programas.
    positions (list[list[int]]): Posiciones de los programas existentes.
    existing_score (int): Ganancia de los programas existentes.
    total_score (int): Ganancia de los nuevos programas.
    final_score (int): Ganancia total.
  """
  try:
    with open(file_path, 'w') as file:
      file.write(f"Ganancia de los programas existentes: {existing_score}\n")
      file.write(f"Ganancia de los nuevos programas: {total_score}\n")
      file.write(f"Ganancia total: {final_score}\n")

      file.write(f"\nPosiciones de los programas existentes:\n")

      for line in positions:
        file.write(f"{line}\n")

      file.write(f"\nNuevas posiciones de los programas:\n")

      for line in new_positions:
        file.write(f"{line}\n")
        
  except Exception as e:
    raise Exception(f"Error al guardar el archivo: {e}")
