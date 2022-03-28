def gridTraveller(rows, cols, memo):
  key=(rows, cols)
  if key in memo : return memo[key]
  if 0 in (rows, cols) : return 0
  if rows == cols == 1 : return 1
  memo[key] = gridTraveller(rows-1, cols, memo)+gridTraveller(rows, cols-1, memo)
  return memo[key]

rows,cols=map(int,input("Enter no.of rows and columns : ").split())
print(gridTraveller(rows, cols, {}))

# Sample input & output :-
'''Enter no.of rows and columns : 50 50
25477612258980856902730428600'''
