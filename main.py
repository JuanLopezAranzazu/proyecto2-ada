import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import timeit
from utils.solver import solve_minizinc_problem
from utils.file_manager import load_data_from_file, save_results_to_file

class App:
  def __init__(self, root):
    self.root = root
    self.root.title("Proyecto 2 ADA II")
    self.root.geometry("800x500")

    # Variables
    self.solvers = ["gecode", "chuffed", "ortools"]
    self.n = None
    self.population = None
    self.enterprise = None
    self.positions = None
    self.new_programs = None
    self.programs = None

    self.create_widgets()

  def create_widgets(self):
    # Crear el marco para la columna de formulario
    self.frame_form = ttk.Frame(self.root, padding="10")
    self.frame_form.grid(row=0, column=0, sticky="nsew")

    # Botón para cargar el archivo
    self.btn_load = ttk.Button(self.frame_form, text="Cargar archivo", command=self.load_file)
    self.btn_load.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

    # Combobox para seleccionar el solver
    ttk.Label(self.frame_form, text="Seleccionar solver:").grid(row=2, column=0, columnspan=2, sticky="ew")
    self.combo_solvers = ttk.Combobox(self.frame_form, values=self.solvers)
    self.combo_solvers.grid(row=3, column=0, columnspan=2, sticky="ew")
    self.combo_solvers.set(self.solvers[0])  # Valor por defecto

    # Botón para ejecutar el modelo
    self.btn_run = ttk.Button(self.frame_form, text="Ejecutar", command=self.run_solver)
    self.btn_run.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    # Crear el marco para la columna de resultados
    self.frame_results = ttk.Frame(self.root, padding="10")
    self.frame_results.grid(row=0, column=1, sticky="nsew")

    # Área de resultados
    self.text_results = tk.Text(self.frame_results, wrap="word", width=50, height=20)
    self.text_results.grid(row=0, column=0, sticky="nsew")

    # Configurar el frame_form para expandirse en ambas direcciones
    self.frame_form.grid_columnconfigure(0, weight=1)  # Permitir crecimiento horizontal

    # Configurar el frame_results para expandirse en ambas direcciones
    self.frame_results.grid_rowconfigure(0, weight=1)  # Permitir crecimiento vertical
    self.frame_results.grid_columnconfigure(0, weight=1)  # Permitir crecimiento horizontal

    # Ajustar el peso de las columnas
    self.root.grid_columnconfigure(0, weight=1)  # Columna del formulario
    self.root.grid_columnconfigure(1, weight=2)  # Columna de resultados

    # Ajustar el peso de las filas
    self.root.grid_rowconfigure(0, weight=1)  # Fila principal

  def load_file(self):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
      try:
        population, enterprise, positions, new_programs, programs, n = load_data_from_file(file_path)
        self.population = population
        self.enterprise = enterprise
        self.positions = positions
        self.new_programs = new_programs
        self.programs = programs
        self.n = n

        # mostrar los datos en el Text widget
        self.text_results.delete(1.0, tk.END)
        self.text_results.insert(tk.END, f"Programas existentes: {programs}\n")
        self.text_results.insert(tk.END, f"Tamaño de las matrices: {n}\n")
        self.text_results.insert(tk.END, f"Cantidad de nuevos programas: {new_programs}\n")

        self.text_results.insert(tk.END, f"Coordenadas de los programas existentes:\n")
        for i in range(programs):
          self.text_results.insert(tk.END, f"{positions[i]}\n")

        self.text_results.insert(tk.END, f"\nMatriz de segmento de población:\n")
        for i in range(n):
          self.text_results.insert(tk.END, f"{population[i]}\n")
        
        self.text_results.insert(tk.END, f"\nMatriz de entorno empresarial:\n")
        for i in range(n):
          self.text_results.insert(tk.END, f"{enterprise[i]}\n")

      except Exception as e:
        self.text_results.delete(1.0, tk.END)
        self.text_results.insert(tk.END, f"Error al cargar el archivo: {e}\n")
        return

  def run_solver(self):
    solver = self.combo_solvers.get()

    # validar que los datos estén cargados
    if not self.population or not self.enterprise or not self.positions or not self.new_programs or not self.programs or not self.n:
      self.text_results.delete(1.0, tk.END)
      self.text_results.insert(tk.END, "Error: Cargar archivo primero\n")
      return

    try:
      start_time = timeit.default_timer()
      result = solve_minizinc_problem(
        solver,
        "./model.mzn",
        self.n,
        self.population,
        self.enterprise,
        self.programs,
        self.positions,
        self.new_programs
      )
      elapsed_time = timeit.default_timer() - start_time

      if not result:
        self.text_results.insert(tk.END, "No se encontró solución\n")
        return
      
      # obtener las nuevas coordenadas de los programas
      new_positions = result["new_positions"]

      # mostrar resultados en el Text widget
      self.text_results.delete(1.0, tk.END)
      self.text_results.insert(tk.END, f"Coordenadas de los nuevos programas:\n")
      
      for position in new_positions:
        self.text_results.insert(tk.END, f"{position}\n")

      self.text_results.insert(tk.END, f"\nTiempo de ejecución: {elapsed_time:.10f} segundos\n")

      # Guardar los resultados en un archivo
      self.save_results(new_positions)
    except Exception as e:
      self.text_results.delete(1.0, tk.END)
      self.text_results.insert(tk.END, f"Error al ejecutar el solver: {e}\n")
      return

  def save_results(self, result_data):
    file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    # poner la extensión si no se proporciona
    if not file_path.endswith(".txt"):
      file_path += ".txt"
    if file_path:
      try:
        save_results_to_file(file_path, result_data)

      except Exception as e:
        self.text_results.insert(tk.END, f"Error al guardar el archivo: {e}\n")

if __name__ == "__main__":
  root = tk.Tk()
  app = App(root)
  root.mainloop()
