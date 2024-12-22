import re

def extract_list(key, text):
  """
  Extraer una lista de enteros de un archivo MiniZinc

  Parámetros:
    key (str): La clave a buscar en el archivo MiniZinc
    text (str): El contenido del archivo MiniZinc
  
  Retorna:
    list: La lista de enteros encontrada en el archivo Mini
  """
  match = re.search(rf"^{key}\s*=\s*\[(.*?)\]$", text, re.MULTILINE)
  if match:
    return [int(num) for num in match.group(1).split(",")]
  return []


def extract_value(key, text):
  """
  Extraer un valor numérico de un archivo MiniZinc

  Parámetros:
    key (str): La clave a buscar en el archivo MiniZinc
    text (str): El contenido del archivo MiniZinc
  
  Retorna:
    int|float|None: El valor numérico encontrado en el archivo MiniZinc
  """
  match = re.search(rf"{key}\s*=\s*([\d.]+)", text)
  if match:
    return float(match.group(1)) if '.' in match.group(1) else int(match.group(1))
  return None


def get_coordinates(vector):
  """
  Obtener las coordenadas de un vector de enteros

  Parámetros:
    vector (list): Un vector de enteros
  
  Retorna:
    list: Una lista de tuplas con las coordenadas de los puntos
  """
  coordinates = [(vector[i], vector[i+1]) for i in range(0, len(vector), 2)]
  return sorted(coordinates, key=lambda coord: coord[0])
