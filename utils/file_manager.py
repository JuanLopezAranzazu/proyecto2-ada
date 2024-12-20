def load_data_from_file(file_path):
  """
  Carga los datos de un archivo de texto y devuelve las matrices y valores.
  """
  try:
    with open(file_path, 'r') as file:
      lines = file.readlines()
      
      population = []
      enterprise = []
      positions = []

      programs = int(lines[0].strip())

      for i in range(programs):
        positions.append(list(map(int, lines[i+1].strip().split())))

      n = int(lines[programs+1].strip())

      for i in range(n):
        population.append(list(map(int, lines[programs+2+i].strip().split())))
        enterprise.append(list(map(int, lines[programs+2+n+i].strip().split())))

      new_programs = int(lines[programs+2+2*n].strip())

      return population, enterprise, positions, new_programs, programs, n

  except Exception as e:
    raise Exception(f"Error al cargar el archivo: {e}")

def save_results_to_file(file_path, result_data):
  """
  Guarda los resultados proporcionados en un archivo de texto.
  """
  try:
    with open(file_path, 'w') as file:
      for line in result_data:
        file.write(f"{line}\n")
        
  except Exception as e:
    raise Exception(f"Error al guardar el archivo: {e}")
