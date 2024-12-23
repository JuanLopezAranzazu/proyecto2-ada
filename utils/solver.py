# Integrantes del grupo:
# - Victor Manuel Álzate Morales - 202313022
# - Juan Esteban López Aránzazu - 202313026
# - Daniel Meléndez Ramirez - 202313024
# - Diego Alejandro Tolosa Sanchez - 202313023

from minizinc import Model, Solver, Instance

def solve_minizinc_problem(solver_name, model_path, n, population, enterprise, programs, positions, new_programs):
  """
  Resuelve un problema de MiniZinc con los datos de entrada proporcionados.

  Parámetros:
    solver_name (str): Nombre del solver a usar (por ejemplo, "gecode").
    model_path (str): Ruta al archivo del modelo MiniZinc.
    n (int): Tamaño de la matriz.
    population (list[list[int]]): Matriz de población.
    enterprise (list[list[int]]): Matriz de entorno empresarial.
    programs (int): Cantidad de programas existentes.
    positions (list[list[int]]): Coordenadas de los programas existentes.
    new_programs (int): Cantidad de nuevos programas a ubicar.

  Retorna:
    result: Resultado de la solución de la instancia.
  """
  try:
    # Crear el modelo
    model = Model(model_path)

    # Crear el solucionador
    solver = Solver.lookup(solver_name)

    # Crear la instancia
    instance = Instance(solver, model)

    # Configurar los datos de entrada
    instance["n"] = n
    instance["population"] = population
    instance["enterprise"] = enterprise
    instance["programs"] = programs
    instance["positions"] = positions
    instance["new_programs"] = new_programs

    # Resolver la instancia
    result = instance.solve()

    return result
  except Exception as e:
    # Lanzar una excepción si ocurre un error
    raise Exception(f"Error al resolver el problema: {e}")
