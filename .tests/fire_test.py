import json
import numpy as np
from spread_fire import spread_fire

def test_fire():
  
  with open('.tests/initial_state.json', 'r') as f:
      grid = json.load(f)
      grid = np.array(grid)
  
  with open('.tests/final_state.json', 'r') as f:
      final_grid = json.load(f)
      final_grid = np.array(final_grid)
  
  for i in range(100):
      update_grid = spread_fire(grid)
      if np.array_equal(update_grid, grid):
          break
      grid = update_grid
  
  assert np.array_equal(final_grid,grid)
