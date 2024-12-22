import unittest
from utils.solver import solve_minizinc_problem
from utils.mzn_parser import extract_list, get_coordinates

class TestSolver(unittest.TestCase):
  def test_solve(self):
    test_cases = [
      {
        'n': 15,
        'population': [
          [4, 0, 1, 1, 2, 2, 0, 0, 4, 15, 15, 4, 11, 2, 1],
          [4, 0, 3, 1, 6, 2, 0, 0, 4, 15, 15, 4, 8, 2, 1],
          [4, 0, 3, 1, 6, 2, 0, 0, 4, 9, 9, 4, 2, 2, 2],
          [0, 0, 1, 1, 21, 23, 4, 4, 4, 16, 16, 4, 2, 2, 2],
          [0, 0, 1, 1, 20, 20, 0, 4, 4, 16, 16, 4, 4, 2, 2],
          [0, 0, 1, 1, 15, 18, 0, 4, 4, 5, 5, 4, 2, 8, 2],
          [0, 0, 1, 1, 2, 2, 4, 0, 4, 16, 16, 4, 2, 7, 1],
          [5, 7, 3, 1, 2, 2, 4, 4, 4, 16, 16, 4, 2, 2, 1],
          [5, 7, 3, 1, 2, 2, 2, 2, 4, 5, 5, 1, 2, 2, 2],
          [5, 7, 9, 1, 2, 2, 14, 14, 14, 16, 16, 4, 2, 2, 2],
          [0, 0, 1, 1, 2, 2, 34, 34, 34, 11, 20, 5, 6, 14, 2],
          [0, 0, 1, 1, 2, 25, 34, 34, 4, 16, 16, 4, 1, 2, 2],
          [0, 0, 4, 1, 2, 25, 34, 34, 4, 16, 16, 4, 2, 2, 2],
          [0, 0, 4, 1, 2, 25, 34, 34, 4, 16, 16, 4, 3, 3, 2],
          [0, 0, 1, 1, 2, 2, 4, 4, 4, 16, 16, 4, 2, 8, 8]
        ],
        'enterprise': [
          [0, 0, 1, 1, 2, 2, 4, 13, 4, 16, 16, 4, 2, 6, 2],
          [0, 0, 1, 1, 2, 2, 4, 13, 4, 16, 16, 4, 2, 6, 2],
          [0, 0, 1, 10, 2, 2, 4, 4, 4, 16, 16, 4, 2, 2, 2],
          [0, 0, 1, 1, 21, 23, 4, 4, 4, 16, 16, 4, 2, 2, 2],
          [0, 0, 1, 1, 20, 20, 4, 4, 4, 16, 16, 4, 4, 5, 2],
          [0, 0, 1, 1, 15, 18, 4, 4, 4, 16, 16, 4, 4, 5, 2],
          [0, 0, 1, 1, 2, 9, 4, 4, 4, 16, 16, 4, 2, 2, 2],
          [18, 18, 1, 1, 9, 2, 11, 4, 4, 16, 16, 4, 2, 2, 2],
          [35, 18, 1, 1, 2, 2, 12, 4, 4, 16, 16, 4, 6, 2, 2],
          [18, 18, 10, 1, 8, 2, 4, 4, 4, 16, 16, 4, 2, 2, 2],
          [0, 0, 1, 1, 2, 2, 4, 4, 4, 16, 16, 4, 2, 14, 2],
          [0, 0, 9, 1, 2, 25, 34, 50, 4, 16, 16, 4, 13, 2, 2],
          [0, 0, 9, 1, 2, 25, 44, 34, 4, 16, 16, 4, 2, 9, 2],
          [0, 0, 1, 1, 5, 25, 34, 34, 4, 16, 16, 4, 2, 9, 2],
          [0, 0, 1, 1, 5, 2, 4, 4, 4, 16, 16, 4, 2, 18, 18]
        ],
        'programs': 3,
        'positions': [[6, 8], [8, 4], [10, 10]],
        'new_programs': 4,
        'solver_name': "gecode",
        'expected': [(14, 6), (12, 8), (14, 8), (12, 6)]
      },
      {
        'n': 10,
        'population': [
          [1, 0, 2, 2, 3, 3, 1, 1, 2, 5],
          [1, 0, 2, 2, 3, 3, 1, 1, 2, 5],
          [1, 0, 2, 2, 3, 3, 1, 1, 2, 5],
          [0, 0, 1, 1, 4, 4, 2, 2, 2, 5],
          [0, 0, 1, 1, 4, 4, 2, 2, 2, 5],
          [0, 0, 1, 1, 3, 3, 2, 2, 2, 5],
          [0, 0, 1, 1, 1, 1, 3, 3, 2, 5],
          [2, 4, 2, 1, 1, 1, 3, 3, 2, 5],
          [2, 4, 2, 1, 1, 1, 3, 3, 2, 5],
          [2, 4, 5, 1, 1, 1, 3, 3, 2, 5]
        ],
        'enterprise': [
          [0, 0, 1, 1, 2, 2, 5, 5, 3, 3],
          [0, 0, 1, 1, 2, 4, 5, 5, 3, 3],
          [0, 0, 2, 1, 2, 4, 5, 5, 3, 3],
          [0, 0, 2, 1, 2, 4, 5, 5, 3, 3],
          [0, 0, 1, 1, 2, 2, 3, 3, 3, 3],
          [0, 0, 1, 1, 2, 2, 3, 4, 3, 3],
          [0, 0, 1, 1, 2, 2, 3, 4, 3, 3],
          [0, 0, 1, 5, 2, 2, 3, 3, 3, 3],
          [0, 0, 1, 1, 4, 4, 3, 3, 3, 3],
          [0, 0, 1, 1, 4, 4, 3, 3, 3, 3]
        ],
        'programs': 3,
        'positions': [[2, 3], [4, 1], [5, 5]],
        'new_programs': 4,
        'solver_name': "gecode",
        'expected': [(7, 9), (5, 9), (3, 9), (3, 5)]
      },
      {
        'n': 18,
        'population': [
          [1, 0, 2, 2, 3, 3, 1, 1, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [1, 0, 2, 2, 3, 3, 1, 1, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 2, 2, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 2, 2, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 3, 3, 2, 2, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [2, 4, 2, 14, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [2, 4, 2, 1, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 2, 2, 5, 5, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 2, 4, 5, 5, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 2, 1, 2, 4, 5, 5, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 2, 1, 2, 4, 5, 5, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 2, 2, 3, 4, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 17, 2, 2, 3, 4, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 5, 2, 2, 3, 3, 3, 33, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7]
        ],
        'enterprise': [
          [0, 0, 1, 1, 4, 44, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 3, 3, 3, 3, 4, 5, 2, 31, 4, 5, 6, 7],
          [2, 0, 1, 1, 4, 4, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [6, 0, 1, 1, 4, 4, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 3, 3, 36, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 4, 4, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [5, 0, 1, 1, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [9, 0, 1, 1, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [7, 0, 1, 1, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7],
          [0, 0, 1, 1, 1, 1, 3, 3, 2, 5, 6, 7, 2, 3, 4, 5, 6, 7]
        ],
        'programs': 5,
        'positions': [[3, 4], [7, 10], [12, 15], [14, 8], [17, 5]],
        'new_programs': 6,
        'solver_name': "chuffed",
        'expected': [(15, 18), (5, 14), (16, 10), (17, 18), (7, 18), (1, 18)]
      }
    ]
    
    for test_case in test_cases:
      with self.subTest(test_case=test_case):
        try:
          result = solve_minizinc_problem(
              test_case['solver_name'],
              "./model.mzn",
              test_case['n'],
              test_case['population'],
              test_case['enterprise'],
              test_case['programs'],
              test_case['positions'],
              test_case['new_programs']
          )

          if not result:
            self.fail(f"No se encontró solución para el caso: {test_case}")

          result_str = str(result)

          new_positions = get_coordinates(extract_list("new_positions", result_str))

          if new_positions is None:
            self.fail(f"El resultado no contiene 'new_positions' para el caso: {test_case}")

          self.assertCountEqual(new_positions, test_case['expected'], 
                                msg=f"Las posiciones no coinciden para el caso: {test_case}")

        except Exception as e:
          self.fail(f"Error durante la prueba del caso {test_case}: {e}")

if __name__ == '__main__':
  unittest.main()
