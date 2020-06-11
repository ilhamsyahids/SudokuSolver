#!/usr/local/bin/python3
import re
from sys import argv
from Sudoku import Sudoku
import load as Loader

if __name__ == "__main__":
  if len(argv) != 2:
    print("USAGE:")
    print("python3 main.py [path]")
    print("OR (UNIX only)")
    print("./main.py [path]")
    exit(0)

  if re.match(r'.*\.png', argv[1]):
    matrix = Loader.loadImage(argv[1])
  elif re.match(r'.*\.txt', argv[1]):
    matrix = Loader.loadText(argv[1])
  else:
    print("Only .png or .txt")
    exit(0)

  sudo = Sudoku(matrix)
  print("Initial Matrix:")
  print(sudo)

  if sudo.solve():
    print("Final Matrix:")
    print(sudo)
    filename = argv[1].split('/')[-1]
    resfilename = re.sub(r'txt|png', 'res.txt', filename)
    with open('../result/' + resfilename, 'w') as f:
      f.write(str(sudo))
      f.close()
  else:
    print("Sudoku is not solvable")
