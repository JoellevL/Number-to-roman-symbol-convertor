# Converter to set a number into a Roman symbol:
  ## Conditions:
    * Eliminate integers < 1 or > 3999  
      - Maximal convertible range: 1 to 3999 (due to the max repetition rule)
    * Logic approach: Greedy Algorithm
  ## Calculations:
    - Calculate division to set the symbol amount.
    - Calculate modulo to set the remainder.
  ## Exceptions: 
    - Dictionary explicitly covers exceptions (4, 9, 40, 90, 400, 900)
